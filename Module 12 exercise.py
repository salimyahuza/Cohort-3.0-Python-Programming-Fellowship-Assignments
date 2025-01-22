paragraph = ('I love teaching. If you do not love teaching what else can you love. '
             'I love Python if you do not love something which can give you all the capabilities '
             'to develop an application what else can you love.')

from collections import Counter
import re

# Clean the paragraph: remove punctuation and convert to lowercase
cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph).lower()

# Split the cleaned paragraph into words
words = cleaned_paragraph.split()

# Count the frequency of each word using Counter
word_counts = Counter(words)

# Get the most common words and their counts
most_common_words = word_counts.most_common()
print("Most frequent words:", most_common_words)

text = ('The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, '
        '0 at origin, 4 and 8 in the positive direction.')

# Extract numbers from the text
numbers = list(map(int, re.findall(r'-?\d+', text)))

# Calculate the distance between the furthest particles
distance = max(numbers) - min(numbers)
print("Particle positions:", numbers)
print("Distance between the furthest particles:", distance)

import re

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'  # Regex for a valid variable name
    return bool(re.match(pattern, variable))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True

text = ('I am a teacher and I love teaching. There is nothing as more rewarding as educating and empowering people. '
        'I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?')

from collections import Counter
import re

# Clean the text: remove punctuation and convert to lowercase
cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

# Split the text into words
words = cleaned_text.split()

# Count word frequencies
word_counts = Counter(words)

# Get the three most frequent words
most_frequent_words = word_counts.most_common(3)
print("Three most frequent words:", most_frequent_words)

