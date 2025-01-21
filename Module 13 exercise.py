# Exercise 1: Counting Lines and Words in Text Files
def count_lines_words(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words

# Example usage:
obama_lines, obama_words = count_lines_words('./data/obama_speech.txt')
michelle_lines, michelle_words = count_lines_words('./data/michelle_obama_speech.txt')
donald_lines, donald_words = count_lines_words('./data/donald_speech.txt')
melina_lines, melina_words = count_lines_words('./data/melina_trump_speech.txt')

print(f"Obama Speech: {obama_lines} lines, {obama_words} words")
print(f"Michelle Obama Speech: {michelle_lines} lines, {michelle_words} words")
print(f"Donald Trump Speech: {donald_lines} lines, {donald_words} words")
print(f"Melina Trump Speech: {melina_lines} lines, {melina_words} words")

# Exercise 2: Finding the Ten Most Spoken Languages
import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    with open(filename, 'r') as file:
        data = json.load(file)
    languages = [language for country in data for language in country['languages']]
    language_counts = Counter(languages)
    most_common_languages = language_counts.most_common(top_n)
    return most_common_languages

# Example usage:
print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))
print(most_spoken_languages(filename='./data/countries_data.json', top_n=3))

# Exercise 3: Finding the Ten Most Populated Countries
import json

def most_populated_countries(filename, top_n):
    with open(filename, 'r') as file:
        data = json.load(file)
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    most_populated = [{'country': country['name'], 'population': country['population']} for country in sorted_countries[:top_n]]
    return most_populated

# Example usage:
print(most_populated_countries(filename='./data/countries_data.json', top_n=10))
print(most_populated_countries(filename='./data/countries_data.json', top_n=3))

# Exercise Level two
# Exercise 4: Extracting Email Addresses
import re

def extract_emails(filename):
    with open(filename, 'r') as file:
        content = file.read()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
    return emails

# Example usage:
emails = extract_emails('./data/email_exchange_big.txt')
print(emails)

# Exercise 5: Finding the Most Common Words
from collections import Counter
import re

def find_most_common_words(text_or_filename, num_words):
    if text_or_filename.endswith('.txt'):
        with open(text_or_filename, 'r') as file:
            text = file.read()
    else:
        text = text_or_filename

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common = word_counts.most_common(num_words)
    return most_common

# Example usage:
print(find_most_common_words('sample.txt', 10))
print(find_most_common_words('sample.txt', 5))

# Exercise 6: Finding the Most Frequent Words in Speeches
# Example usage:
print(find_most_common_words('./data/obama_speech.txt', 10))
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))
print(find_most_common_words('./data/donald_speech.txt', 10))
print(find_most_common_words('./data/melina_trump_speech.txt', 10))

# Exercise 7: Checking Text Similarity
import re
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def clean_text(text):
    text = re.sub(r'\W+', ' ', text.lower())
    return text

def remove_support_words(text):
    words = text.split()
    filtered_words = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return ' '.join(filtered_words)

def check_text_similarity(text1, text2):
    text1 = clean_text(text1)
    text2 = clean_text(text2)
    text1 = remove_support_words(text1)
    text2 = remove_support_words(text2)
    
    words1 = Counter(text1.split())
    words2 = Counter(text2.split())
    
    common_words = set(words1.keys()) & set(words2.keys())
    similarity = sum(min(words1[word], words2[word]) for word in common_words)
    
    return similarity

# Example usage:
with open('./data/michelle_obama_speech.txt', 'r') as file:
    michelle_speech = file.read()

with open('./data/melina_trump_speech.txt', 'r') as file:
    melina_speech = file.read()

similarity_score = check_text_similarity(michelle_speech, melina_speech)
print(f"Similarity score: {similarity_score}")

# Exercise 8: Finding the Most Repeated Words in Romeo and Juliet
# Example usage:
print(find_most_common_words('./data/romeo_and_juliet.txt', 10))

# Exercise 9: Analyzing Hacker News CSV File
import csv

def count_lines_with_keywords(filename, keywords):
    counts = {keyword: 0 for keyword in keywords}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            line = ' '.join(row).lower()
            for keyword in keywords:
                if keyword.lower() in line:
                    counts[keyword] += 1
    return counts

# Example usage:
keywords = ['python', 'javascript', 'java']
counts = count_lines_with_keywords('./data/hacker_news.csv', keywords)
print(f"Lines containing 'python': {counts['python']}")
print(f"Lines containing 'javascript': {counts['javascript']}")
print(f"Lines containing 'java' but not 'javascript': {counts['java'] - counts['javascript']}")

