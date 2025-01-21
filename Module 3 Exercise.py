# Declare your age as an integer variable
age = 40

# Declare your height as a float variable
height = 5.9

# Declare a variable that stores a complex number
complex_number = 3 + 4j

# Calculate the area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Calculate the perimeter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Calculate the area and perimeter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

# Calculate the area and circumference of a circle
radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

# Calculate the slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
x_intercept = -2 / 2
y_intercept = -2
print(f"Slope: {slope}, x-intercept: {x_intercept}, y-intercept: {y_intercept}")

# Find the slope and Euclidean distance between points (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Slope: {slope}, Euclidean distance: {distance}")

# Compare the slopes in tasks 8 and 9
slope_task_8 = 2
slope_task_9 = (10 - 2) / (6 - 2)
print(f"Slope in task 8: {slope_task_8}, Slope in task 9: {slope_task_9}")

# Calculate the value of y (y = x^2 + 6x + 9) and find x when y is 0
def calculate_y(x):
    return x**2 + 6*x + 9

x_values = [-3, 0, 3]  # Try different x values
for x in x_values:
    y = calculate_y(x)
    print(f"For x = {x}, y = {y}")

# Finding x when y is 0
import sympy as sp
x = sp.symbols('x')
solutions = sp.solve(x**2 + 6*x + 9, x)
print(f"x values when y is 0: {solutions}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
len_python = len('python')
len_dragon = len('dragon')
print(f"Length of 'python': {len_python}, Length of 'dragon': {len_dragon}")
print(f"Falsy comparison: {len_python == len_dragon}")

# Check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)

# Check if 'on' is not in both 'dragon' and 'python'
print('on' not in 'dragon' and 'on' not in 'python')

# Find the length of 'python', convert to float, and then to string
length_python = len('python')
length_float = float(length_python)
length_str = str(length_float)
print(f"Length as float: {length_float}, Length as string: {length_str}")

# Check if a number is even
number = int(input("Enter a number: "))
is_even = number % 2 == 0
print(f"Is the number even? {is_even}")

# Check if floor division of 7 by 3 is equal to int converted value of 2.7
result = 7 // 3 == int(2.7)
print(result)

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
try:
    result = int('9.8') == 10
except ValueError:
    result = False
print(result)

# Calculate pay based on hours and rate per hour
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print(f"Your weekly earning is {pay}")

# Calculate the number of seconds a person can live
years_lived = int(input("Enter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds = years_lived * seconds_in_a_year
print(f"You have lived for {total_seconds} seconds.")

# Display a table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
