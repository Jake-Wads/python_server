#: # 20 Python Data Structure Manipulation Exercises
#:
#: The following questions reference the `students` dataframe below.
#:
#: Write the python code to answer the following questions:
#:
#: 1. How many students are there?
#: 1. How many students prefer light coffee? For each type of coffee roast?
#: 1. How many types of each pet are there?
#: 1. How many grades does each student have? Do they all have the same number of
#:    grades?
#: 1. What is each student's grade average?
#: 1. How many pets does each student have?
#: 1. How many students are in web development? data science?
#: 1. What is the average number of pets for students in web development?
#: 1. What is the average pet age for students in data science?
#: 1. What is most frequent coffee preference for data science students?
#: 1. What is the least frequent coffee preference for web development students?
#: 1. What is the average grade for students with at least 2 pets?
#: 1. How many students have 3 pets?
#: 1. What is the average grade for students with 0 pets?
#: 1. What is the average grade for web development students? data science
#:    students?
#: 1. What is the average grade range (i.e. highest grade - lowest grade) for
#:    dark coffee drinkers?
#: 1. What is the average number of pets for medium coffee drinkers?
#: 1. What is the most common type of pet for web development students?
#: 1. What is the average name length?
#: 1. What is the highest pet age for light coffee drinkers?

import random as r

import numpy as np
import pandas as pd

np.random.seed(123)
r.seed(123)

names = [
    "Ada Lovelace",
    "Thomas Bayes",
    "Marie Curie",
    "Grace Hopper",
    "Alan Turing",
    "Rosalind Franklin",
    "Elizabeth Blackwell",
    "Rene Descartes",
    "Ahmed Zewail",
    "Chien-Shiung Wu",
    "William Sanford Nye",
    "Carl Sagan",
    "Jane Goodall",
    "Richard Feynman",
]

n = len(names)

df = pd.DataFrame(
    {
        "name": names,
        "grades": [[r.randint(70, 100) for _ in range(4)] for _ in range(n)],
        "pets": [
            [
                {"species": r.choice(["cat", "dog"]), "age": r.randint(0, 9)}
                for _ in range(4)
                if r.choice([0, 0, 1])
            ]
            for _ in range(n)
        ],
        "coffee_preference": np.random.choice(["light", "medium", "dark"], n),
        "course": np.random.choice(["webdev", "data science"], n),
    }
)

df.query("coffee_preference == 'light'").pets.apply(lambda l: [p["age"] for p in l])

pd.Series(np.arange(0, 20, 0.5)).apply(round)
