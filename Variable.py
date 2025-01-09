# Day 2: 30 Days of python programming

# Declaring variables
first_name = "John"  # Replace "John" with your first name
last_name = "Doe"  # Replace "Doe" with your last name
full_name = first_name + " " + last_name
country = "Nigeria"  # Replace "Nigeria" with your country
city = "Katsina"  # Replace "Katsina" with your city
age = 25  # Replace 25 with your age
year = 2025  # Replace 2025 with the current year
is_married = False  # Replace False with True if married
is_true = True
is_light_on = False

# Declaring multiple variables in one line
a, b, c = 5, 10, 15

# Printing to verify the values (Optional)
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("Multiple Variables:", a, b, c)

# Day 2: 30 Days of python programming - Level 2 Exercises

# Variables from Level 1
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
country = "Nigeria"
city = "Katsina"
age = 25
year = 2025
is_married = False
is_true = True
is_light_on = False
a, b, c = 5, 10, 15

# Check the data type of all variables using type()
print("Data Types:")
print("First Name:", type(first_name))
print("Last Name:", type(last_name))
print("Full Name:", type(full_name))
print("Country:", type(country))
print("City:", type(city))
print("Age:", type(age))
print("Year:", type(year))
print("Is Married:", type(is_married))
print("Is True:", type(is_true))
print("Is Light On:", type(is_light_on))
print("Multiple Variables (a, b, c):", type(a), type(b), type(c))

# Using len() to find the length of first name
print("\nLength of First Name:", len(first_name))

# Comparing the length of first name and last name
print("Is first name longer than last name?", len(first_name) > len(last_name))

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("\nArithmetic Operations:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Calculating area and circumference of a circle
radius = 30
pi = 3.14159
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("\nCircle Calculations:")
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# Take radius as user input and calculate area
radius = float(input("\nEnter the radius of the circle: "))
area_of_circle_user = pi * radius ** 2
print("Area of Circle (User Input):", area_of_circle_user)

# Getting user input for personal details
first_name = input("\nEnter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("\nUser Input:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

# Run help('keywords') to display Python reserved keywords
print("\nPython Reserved Keywords:")
help('keywords')
