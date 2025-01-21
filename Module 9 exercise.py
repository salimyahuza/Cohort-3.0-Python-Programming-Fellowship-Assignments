# A function to add two numbers
def add_two_numbers(a, b):
    return a + b

# A function to calculate the area of a circle
import math

def area_of_circle(r):
    return math.pi * r * r
# Function to sum arbitrary number of arguments
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "All arguments must be numbers."

# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Function to check the season based on the month
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'

# Function to calculate the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Slope is undefined'
    return (y2 - y1) / (x2 - x1)

# Function to solve a quadratic equation
import cmath

def solve_quadratic_eqn(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    return sol1, sol2

# Function to print each element of a list
def print_list(lst):
    for item in lst:
        print(item)

# Function to reverse a list
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Function to capitalize list items
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# Function to add an item to a list
def add_item(lst, item):
    lst.append(item)
    return lst

# Function to remove an item from a list
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# Function to sum numbers in a range
def sum_of_numbers(n):
    return sum(range(1, n+1))

# Function to sum odd numbers in a range
def sum_of_odds(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

# Function to sum even numbers in a range
def sum_of_even(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)

# Exercise level two
# Function to count evens and odds
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of odds are {odds}. The number of evens are {evens}."

print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

# Function to check if a parameter is empty
def is_empty(param):
    return not bool(param)

print(is_empty([]))  # True
print(is_empty([1, 2, 3]))  # False

# Functions to calculate mean, median, mode, range, variance, and standard deviation
import statistics

def calculate_mean(lst):
    return statistics.mean(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)

numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6]

print(calculate_mean(numbers))  # 3.6666666666666665
print(calculate_median(numbers))  # 4
print(calculate_mode(numbers))  # 5
print(calculate_range(numbers))  # 5
print(calculate_variance(numbers))  # 3.5277777777777777
print(calculate_std(numbers))  # 1.878672873255453

# Exercise level three
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # True
print(is_prime(4))   # False

# Function to check if all items in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1, 2, 3, 4]))  # True
print(all_unique([1, 2, 2, 4]))  # False

# Function to check if all items in a list are of the same data type
def all_same_type(lst):
    return all(isinstance(i, type(lst[0])) for i in lst)

print(all_same_type([1, 2, 3, 4]))  # True
print(all_same_type([1, '2', 3, 4]))  # False

# Function to check if a variable name is valid in Python
import keyword

def is_valid_variable(var):
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True

print(is_valid_variable('variable1'))  # True
print(is_valid_variable('1variable'))  # False
print(is_valid_variable('for'))        # False

# Functions to get the most spoken languages and most populated countries
# Assuming countries_data.py contains a list of dictionaries with country data
from countries_data import countries_data

def most_spoken_languages(n=10):
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

def most_populated_countries(n=10):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:n]

# Example usage:
print(most_spoken_languages(10))
print(most_populated_countries(10))
