# Eercise level 1
# Exercise 1: Generating a Six-Digit/Character Random User ID
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

# Example usage:
print(random_user_id())

# Exercise 2: Generating User IDs Based on User Input
def user_id_gen_by_user():
    num_chars = int(input("Enter the number of characters: "))
    num_ids = int(input("Enter the number of IDs: "))
    characters = string.ascii_letters + string.digits
    user_ids = [''.join(random.choices(characters, k=num_chars)) for _ in range(num_ids)]
    return user_ids

# Example usage:
for user_id in user_id_gen_by_user():
    print(user_id)

# Exercise 3: Generating RGB Colors
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Example usage:
print(rgb_color_gen())

# Exercise level 2
# Exercise 1: Generating Hexadecimal Colors
import random

def list_of_hexa_colors(num_colors):
    hexa_colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hexa_colors.append(color)
    return hexa_colors

# Example usage:
print(list_of_hexa_colors(3))
print(list_of_hexa_colors(1))

# Exercise 2: Generating RGB Colors
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        color = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
        rgb_colors.append(color)
    return rgb_colors

# Example usage:
print(list_of_rgb_colors(3))
print(list_of_rgb_colors(1))

# Exercise 3: Generating Hexa or RGB Colors
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."

# Example usage:
print(generate_colors('hexa', 3))  # ['#a3e12f','#03ed55','#eb3d2b']
print(generate_colors('hexa', 1))  # ['#b334ef']
print(generate_colors('rgb', 3))   # ['rgb(5, 55, 175)','rgb(50, 105, 100)','rgb(15, 26, 80)']
print(generate_colors('rgb', 1))   # ['rgb(33,79,176)']

# Exercise level 3
# Exercise 1: Shuffling a List
import random

def shuffle_list(lst):
    shuffled_list = lst[:]
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Exercise 2: Generating Unique Random Numbers
def unique_random_numbers():
    return random.sample(range(10), 7)

# Example usage:
print(unique_random_numbers())


# Virtual Environment Exercises
# Create a project directory
mkdir my_project
cd my_project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate

# Install necessary packages (if any)
pip install <package_name>

# Deactivate the virtual environment when done
deactivate

