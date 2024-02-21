#!/usr/bin/env python3

import json
import random


def partition(xs: list, chunksize: int):
    """
    Partition a sequence into smaller subsequences

    Returns a generator that yields the smaller partitions

    >>> letters = 'abcdefghijklm'
    >>> partition(letters, 2)
    <generator object partition at ...>
    >>> list(partition(letters, 2))
    ['ab', 'cd', 'ef', 'gh', 'ij', 'kl', 'm']
    >>> list(partition(letters, 3))
    ['abc', 'def', 'ghi', 'jkl', 'm']
    """
    for i in range(0, len(xs), chunksize):
        yield xs[i : i + chunksize]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("cohort")
    parser.add_argument(
        "-f",
        "--students-file",
        default="./grading/students.json",
        help="Path to the json file that holds student info",
    )
    parser.add_argument(
        "-s", "--group-size", type=int, default=4, help="size of the groups to create"
    )
    parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter
    args = parser.parse_args()

    cohorts = json.load(open(args.students_file))

    students = cohorts[args.cohort]

    random.shuffle(students)

    for i, group in enumerate(partition(students, args.group_size)):
        print(f"--- Group {i + 1}")
        for student in group:
            print(f'  - {student["name"]}')
