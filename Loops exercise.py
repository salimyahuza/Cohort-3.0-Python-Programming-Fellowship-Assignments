# Level 1
# Iterate 0 to 10 using for loop, do the same using while loop
# Using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1

# Iterate 10 to 0 using for loop, do the same using while loop
# Using for loop
for i in range(10, -1, -1):
    print(i)

# Using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get the following triangle
for i in range(1, 8):
    print('#' * i)

# Use nested loops to create the following pattern
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# Print the following pattern
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterate through the list using a for loop and print out the items
items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)

# Exercise level 2
# Sum of all numbers from 0 to 100
sum_all_numbers = 0
for i in range(101):
    sum_all_numbers += i
print(f"The sum of all numbers is {sum_all_numbers}.")

# Sum of all evens and the sum of all odds from 0 to 100
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i
print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")

# Exercise level 3
# Loop through the countries and extract all the countries containing the word 'land'
countries = [
    "Finland", "Sweden", "Norway", "Denmark", "Iceland", "Ireland", "Poland", 
    "Netherlands", "Switzerland", "Thailand", "New Zealand", "England"
]

countries_with_land = [country for country in countries if 'land' in country.lower()]
print(f"Countries containing 'land': {countries_with_land}")

# Reverse the order of the fruit list using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print(f"Reversed fruits list: {reversed_fruits}")

# Analyze countries_data
# Total number of languages in the data
countries_data = [
    {"country": "Afghanistan", "languages": ["Pashto", "Uzbek", "Turkmen"], "population": 27657145},
    {"country": "Albania", "languages": ["Albanian"], "population": 2886026},
    {"country": "Algeria", "languages": ["Arabic"], "population": 40400000},
    {"country": "Andorra", "languages": ["Catalan"], "population": 78014},
    {"country": "Angola", "languages": ["Portuguese"], "population": 25868000},
    # ... (more countries data)
]

all_languages = set()
for country in countries_data:
    for language in country["languages"]:
        all_languages.add(language)
total_languages = len(all_languages)
print(f"Total number of languages: {total_languages}")

# Find the ten most spoken languages from the data
from collections import Counter

language_counter = Counter()
for country in countries_data:
    for language in country["languages"]:
        language_counter[language] += 1

most_spoken_languages = language_counter.most_common(10)
print(f"Ten most spoken languages: {most_spoken_languages}")

# Find the 10 most populated countries in the world
most_populated_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)[:10]
print("Ten most populated countries:")
for country in most_populated_countries:
    print(f"{country['country']}: {country['population']}")

