# Grading

## Exercise Checker

There are three important files in this directory pertaining to exercise grades

- `check_exercises.py`: the python script that calculates students' exercise
  grades

    Run it like so:

    ```
    cd grading
    python check_exercises.py --help
    ```

    To see usage instructions.

    The script will clone all of the students github repos to a temporary
    directory to check for the presence of all the files we have listed.

- `exercise_list.json`: Where all the exercises by github repo are listed out

    The keys in this object are the names of the github repositories, and the
    values are a list of the files that should be in the repo.

    This file lists all of the names of the exercises by module. If the file
    name has a file extension, then we are looking for specifically that file,
    if there is no extension, either a python script or a jupyter notebook is
    allowed.

- `students.json`: a list of students

    The keys in this object are cohort names, and the values are a list of
    objects, where each object represents a student.
