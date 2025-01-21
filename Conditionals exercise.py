# Exercise level 1
# Get user input for age and provide feedback
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Compare the values of my_age and your_age
my_age = 25  # Replace with your actual age
your_age = int(input("Enter your age: "))

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user and compare them
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Exercise level 2
# Grade students according to their scores
score = int(input("Enter your score: "))

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Invalid score'

print(f"Your grade is: {grade}")

# Check the season based on user input
month = input("Enter the month: ").capitalize()

if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Invalid month'

print(f"The season is: {season}")

# Check if a fruit exists in the list and add it if it doesn't
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_add = input("Enter a fruit: ").lower()

if fruit_to_add in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit_to_add)
    print(f"Modified list: {fruits}")

# Exercise level 3
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print(f"Middle skill: {middle_skill}")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

# Determine the person's title based on their skills
if 'skills' in person:
    skills_set = set(person['skills'])
    if skills_set == {'JavaScript', 'React'}:
        title = "He is a front end developer"
    elif skills_set >= {'Node', 'Python', 'MongoDB'}:
        title = "He is a backend developer"
    elif skills_set >= {'React', 'Node', 'MongoDB'}:
        title = "He is a fullstack developer"
    else:
        title = "unknown title"
    print(title)

# If the person is married and if he lives in Nigeria, print his information
if person['is_marred'] and person['country'] == 'Nigeria':
    print(f"{person['first_name']} {person['last_name']} lives in Nigeria. He is married.")
