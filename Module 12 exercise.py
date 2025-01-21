# Level one exercise
# Most frequent word in the paragraph: I analyzed the paragraph and found the most frequent words along with their counts
paragraph = ('I love teaching. If you do not love teaching what else can you love. '
             'I love Python if you do not love something which can give you all the capabilities '
             'to develop an application what else can you love.')

from collections import Counter
import re

# Remove punctuation and convert to lowercase
cleaned_paragraph = re.sub(r'[^\\w\\s]', '', paragraph).lower()

# Split the paragraph into words
words = cleaned_paragraph.split()

# Count the frequency of each word
word_counts = Counter(words)

# Get the most common words
most_common_words = word_counts.most_common()
print(most_common_words)

# Distance between the two furthest particles: I extracted the numbers from the text and calculated the distance between the two furthest particles
text = ('The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, '
        '0 at origin, 4 and 8 in the positive direction.')

# Extract numbers from the text
numbers = list(map(int, re.findall(r'-?\\d+', text)))

# Find the distance between the two furthest particles
distance = max(numbers) - min(numbers)
print(numbers)
print(distance)

# A function that uses a regular expression to check if a string is a valid Python variable name
import re

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True

# Exercise level 3
# I cleaned the text and counted the three most frequent words in the string
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# Most Frequent Words:
[('I', 3), ('a', 2), ('teacher', 2)]
