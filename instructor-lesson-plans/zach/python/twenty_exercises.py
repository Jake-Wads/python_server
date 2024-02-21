students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{
            "species": "horse",
            "age": 8
        }],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{
            "species": "cat",
            "age": 0
        }],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{
            "species": "dog",
            "age": 4
        }, {
            "species": "cat",
            "age": 4
        }],
    },
    {
        "id":
        "100005",
        "student":
        "Alan Turing",
        "coffee_preference":
        "dark",
        "course":
        "web development",
        "grades": [78, 98, 85, 65],
        "pets": [{
            "species": "horse",
            "age": 6
        }, {
            "species": "horse",
            "age": 7
        }, {
            "species": "dog",
            "age": 5
        }],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{
            "species": "cat",
            "age": 10
        }],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{
            "species": "cat",
            "age": 10
        }, {
            "species": "cat",
            "age": 8
        }],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{
            "species": "cat",
            "age": 0
        }, {
            "species": "cat",
            "age": 0
        }],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{
            "species": "cat",
            "age": 8
        }],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{
            "species": "cat",
            "age": 8
        }, {
            "species": "cat",
            "age": 5
        }],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{
            "species": "cat",
            "age": 10
        }],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{
            "species": "horse",
            "age": 4
        }],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{
            "species": "dog",
            "age": 6
        }],
    },
]

# How many students are there?
len(students)

# How many students prefer light coffee? For each type of coffee roast?
len([s for s in students if s["coffee_preference"] == "light"])
{
    p: len([s for s in students if s["coffee_preference"] == p])
    for p in ["light", "medium", "dark"]
}

# How many types of each pet are there?
pets = [s["pets"] for s in students]
pets = sum(pets, [])  # flatten the list
{
    species: len([p for p in pets if p["species"] == species])
    for species in set(pet_species)
}

# How many grades does each student have? Do they all have the same number of grades?
[s["grades"] == 4 for s in students]
all([len(s["grades"]) == 4 for s in students])

# Avg grade for each student
{s["student"]: sum(s["grades"]) / len(s["grades"]) for s in students}
# num of pets for each student
[(s["student"], len(s["pets"])) for s in students]

# How many students are in web development? data science?
{
    course: len([s for s in students if s["course"] == course])
    for course in ["data science", "web development"]
}

# What is the average number of pets for students in web development?
webdev_students = [s for s in students if s["course"] == "web development"]
webdev_n_pets = [len(s["pets"]) for s in webdev_students]
sum(webdev_n_pets) / len(webdev_n_pets)

# What is the average pet age for students in data science?
ds_students = [s for s in students if s["course"] == "data science"]
ds_students_pet_ages = sum(
    [[pet["age"] for pet in s["pets"]] for s in ds_students], [])
sum(ds_students_pet_ages) / len(ds_students_pet_ages)

# What is most frequent coffee preference for data science students?
max(
    [(p, len([s for s in ds_students if s["coffee_preference"] == p]))
     for p in ["light", "medium", "dark"]],
    key=lambda t: t[1],
)

# What is the least frequent coffee preference for web development students?
min(
    [(p, len([s for s in webdev_students if s["coffee_preference"] == p]))
     for p in ["light", "medium", "dark"]],
    key=lambda t: t[1],
)

# What is the average grade for students with at least 2 pets?
avg_grades = [
    sum(s["grades"]) / len(s["grades"]) for s in students
    if len(s["pets"]) >= 2
]
sum(avg_grades) / len(avg_grades)

# How many students have 3 pets?
len([s for s in students if len(s["pets"]) == 3])

# What is the average grade for students with 0 pets?
avg_grades = [
    sum(s["grades"]) / len(s["grades"]) for s in students
    if len(s["pets"]) == 0
]
sum(avg_grades) / len(avg_grades)

# What is the average grade for web development students? data science students?
ds_avg_grades = [sum(s["grades"]) / len(s["grades"]) for s in ds_students]
wd_avg_grades = [sum(s["grades"]) / len(s["grades"]) for s in webdev_students]
sum(ds_avg_grades) / len(ds_avg_grades)
sum(wd_avg_grades) / len(wd_avg_grades)

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
grade_ranges = [
    max(s["grades"]) - min(s["grades"]) for s in students
    if s["coffee_preference"] == "dark"
]
sum(grade_ranges) / len(grade_ranges)

# What is the average number of pets for medium coffee drinkers?
n_pets = [
    len(s["pets"]) for s in students if s["coffee_preference"] == "medium"
]
sum(n_pets) / len(n_pets)

# What is the most common type of pet for web development students?
wd_pets = sum(
    [[pet["species"] for pet in s["pets"]]
     for s in students if s["course"] == "web development"],
    [],
)
{
    species: len([pet for pet in wd_pets if pet == species])
    for species in ["dog", "cat", "horse"]
}

# What is the average name length?
name_lengths = [len(s["student"]) for s in students]
sum(name_lengths) / len(name_lengths)

# What is the highest pet age for light coffee drinkers?
pet_ages = sum(
    [[pet["age"] for pet in s["pets"]]
     for s in students if s["coffee_preference"] == "light"],
    [],
)
max(pet_ages)
