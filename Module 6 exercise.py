# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# Get the length of the student dictionary
student_length = len(student)
print(f"Length of student dictionary: {student_length}")

# Get the value of skills and check the data type, it should be a list
skills = student['skills']
skills_type = type(skills)
print(f"Skills: {skills}, Type: {skills_type}")

# Modify the skills values by adding one or two skills
student['skills'].extend(['C++', 'JavaScript'])
print(f"Updated skills: {student['skills']}")

# Get the dictionary keys as a list
student_keys = list(student.keys())
print(f"Student dictionary keys: {student_keys}")

# Get the dictionary values as a list
student_values = list(student.values())
print(f"Student dictionary values: {student_values}")

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(f"Student dictionary as list of tuples: {student_items}")

# Delete one of the items in the dictionary
del student['address']
print(f"Student dictionary after deleting address: {student}")

# Delete one of the dictionaries
del dog
print("Dog dictionary deleted.")
