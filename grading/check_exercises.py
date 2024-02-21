import os
import json
import logging
from os import path
from tempfile import TemporaryDirectory
from typing import List, NamedTuple

Student = NamedTuple('Student', [('id', int), ('username', str), ('name', str)])
ExerciseGrade = NamedTuple('ExerciseGrade', [('score', float),
                                             ('missing_files', List[str]),
                                             ('project', str),
                                             ('student', Student)])

EXERCISES = json.load(open('./exercise_list.json'))
STUDENTS = json.load(open('./students.json'))


# This environment variable tells git not to prompt for a username and password.
# By default, if a github repo is not found, git will prompt for credentials
# (assuming that the repo is a private repo that requires authentication). This
# breaks our grading script, and all of the repos we want to access should be
# public, so we will force an error in this scenario. See
# https://serverfault.com/questions/544156/git-clone-fail-instead-of-prompting-for-credentials
# and
#     $ man -P less\ +/GIT_TERMINAL_PROMPT git
os.environ['GIT_TERMINAL_PROMPT'] = '0'


def get_github_url(username: str, repo: str) -> str:
    return f'https://github.com/{username}/{repo}.git'


def exercise_file_exists(file: str, tempdir: str):
    exact = file.endswith('.py') or file.endswith('.ipynb') or file.endswith('.sql')
    if exact:
        return path.exists(f'{tempdir}/{file}')
    else:
        return any([path.exists(f'{tempdir}/{file}.{ext}') for ext in ['py', 'ipynb']])


def check_exercises(student: Student, project: str) -> ExerciseGrade:
    logging.info(f'Checking {project} exercises for {student}')
    with TemporaryDirectory() as tempdir:
        repo_url = get_github_url(student.username, project)
        cmd = f'git clone {repo_url} {tempdir}'
        logging.debug(cmd)
        os.system(cmd)
        exercise_files = EXERCISES[project]
        missing_files = [
            file for file in exercise_files
            if not exercise_file_exists(file, tempdir)
        ]
        n_total_exercises = len(exercise_files)
        n_completed_exercises = n_total_exercises - len(missing_files)
        score = n_completed_exercises / n_total_exercises
        return ExerciseGrade(score, missing_files, project, student)


def print_detail(grade: ExerciseGrade):
    repo_url = get_github_url(grade.student.username, grade.project)
    missing_files = '\n'.join(
        [f'    - {file}' for file in grade.missing_files])
    print(f'Student: {grade.student.name} Username: {grade.student.username}')
    print(f'  - Score: {grade.score}')
    print(f'  - Repo: {repo_url}')
    print('  - Missing Files')
    print(missing_files)
    print()


def print_csv(grades: List[ExerciseGrade]):
    print('name,github_username,project,score')
    row = '{},{},{},{}'
    for grade in grades:
        print(row.format(grade.student.name, grade.student.username,
                         grade.project, grade.score))


def print_csv_details(grades: List[ExerciseGrade]):
    print('id,github_username,name,file,present')
    exercises = EXERCISES[grades[0].project]
    for grade in grades:
        for exercise in exercises:
            present = not exercise in grade.missing_files
            output = str(grade.student.id) + ','
            output+= grade.student.username + ','
            output+= grade.student.name + ','
            output+= exercise + ','
            output+= str(present)
            print(output)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.description = 'Check exercise completion % for students'
    parser.add_argument('-p', '--project', required=True, choices=EXERCISES.keys(),
                        help='The project to check exercise completion on')
    parser.add_argument('-c', '--cohort', required=True, choices=STUDENTS.keys(),
                        help='The cohort to check exercises for')
    parser.add_argument('-v', '--verbose', help='increase output verbosity',
                        action='count')
    parser.add_argument('--format', choices=('csv', 'detail', 'csvdetail'), default='csv',
                        help='output format, detail shows missing exercises')
    args = parser.parse_args()

    if args.verbose is None:
        loglevel = logging.WARN
    elif args.verbose == 1:
        loglevel = logging.INFO
    elif args.verbose >= 2:
        loglevel = logging.DEBUG
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=loglevel)

    students: List[Student] = [Student(**student)
                               for student in STUDENTS[args.cohort]]
    grades: List[ExerciseGrade] = [check_exercises(student, args.project)
                                   for student in students]

    if args.format == 'csv':
        print_csv(grades)
    elif args.format == 'csvdetail':
        print_csv_details(grades)
    elif args.format == 'detail':
        for grade in grades:
            print_detail(grade)
