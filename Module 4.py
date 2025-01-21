# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string
concatenated_string = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(concatenated_string)

# Concatenate the string 'Coding', 'For', 'All' to a single string
concatenated_string = ' '.join(['Coding', 'For', 'All'])
print(concatenated_string)

# Declare a variable named company and assign it to an initial value "Coding For All
company = "Coding For All"

# Print the variable company using print()
print(company)

# Print the length of the company string using len() method and print()
print(len(company))

# Change all the characters to uppercase letters using upper() method
print(company.upper())

# Change all the characters to lowercase letters using lower() method
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string
first_word = company.split()[0]
print(first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods
contains_coding = 'Coding' in company
print(contains_coding)

# Replace the word coding in the string 'Coding For All' to Python
new_string = company.replace('Coding', 'Python')
print(new_string)

# Change Python for Everyone to Python for All using the replace method or other methods
phrase = "Python for Everyone"
new_phrase = phrase.replace('Everyone', 'All')
print(new_phrase)

# Split the string 'Coding For All' using space as the separator (split())
split_string = company.split()
print(split_string)

# Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = tech_companies.split(', ')
print(split_companies)

# What is the character at index 0 in the string Coding For All
print(company[0])

# What is the last index of the string Coding For All
print(len(company) - 1)

# What character is at index 10 in "Coding For All" string
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'
acronym = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'
acronym = ''.join([word[0] for word in 'Coding For All'.split()])
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All
position_C = company.index('C')
print(position_C)

# Use index to determine the position of the first occurrence of F in Coding For All
position_F = company.index('F')
print(position_F)

# Use rfind to determine the position of the last occurrence of l in Coding For All People
phrase = "Coding For All People"
last_l_position = phrase.rfind('l')
print(last_l_position)

# Use index or find to find the position of the first occurrence of the word 'because' in the sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_because_position = sentence.find('because')
print(first_because_position)

# Use rindex to find the position of the last occurrence of the word because in the sentence
last_because_position = sentence.rindex('because')
print(last_because_position)

# Slice out the phrase 'because because because' in the sentence
sliced_sentence = sentence.replace('because because because', '')
print(sliced_sentence)

# Find the position of the first occurrence of the word 'because' in the sentence
first_because_position = sentence.find('because')
print(first_because_position)

# Slice out the phrase 'because because because' in the sentence
sliced_sentence = sentence.replace('because because because', '')
print(sliced_sentence)

# Does 'Coding For All' start with a substring Coding?
starts_with_coding = company.startswith('Coding')
print(starts_with_coding)

# Does 'Coding For All' end with a substring coding?
ends_with_coding = company.endswith('coding')
print(ends_with_coding)

# Remove the left and right trailing spaces in the string ' Coding For All '
trimmed_string = '   Coding For All      '.strip()
print(trimmed_string)

# Which one of the following variables return True when we use the method isidentifier()
print("30DaysOfPython".isidentifier())  # False
print("thirty_days_of_python".isidentifier())  # True

# Join the list with a hash with space string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = ' # '.join(libraries)
print(joined_libraries)

# Use the new line escape sequence to separate the following sentences
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Make the following using string formatting methods
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

