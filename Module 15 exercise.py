# Task 1: Finding the 10 Most Frequent Words in "Romeo and Juliet"
import requests
from collections import Counter
import re

def get_text_from_url(url):
    response = requests.get(url)
    return response.text

def find_most_common_words(text, num_words):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common = word_counts.most_common(num_words)
    return most_common

romeo_and_juliet_url = 'http://www.gutenberg.org/files/1112/1112.txt'
text = get_text_from_url(romeo_and_juliet_url)
most_common_words = find_most_common_words(text, 10)
print(most_common_words)

# Task 2: Analyzing the Cats API
import requests
import statistics

def get_cats_data(url):
    response = requests.get(url)
    return response.json()

cats_api = 'https://api.thecatapi.com/v1/breeds'
cats_data = get_cats_data(cats_api)

# I. Weight Analysis
weights = [float(cat['weight']['metric'].split(' - ')[0]) for cat in cats_data]
min_weight = min(weights)
max_weight = max(weights)
mean_weight = statistics.mean(weights)
median_weight = statistics.median(weights)
std_dev_weight = statistics.stdev(weights)

print(f"Weight (kg) - Min: {min_weight}, Max: {max_weight}, Mean: {mean_weight}, Median: {median_weight}, Std Dev: {std_dev_weight}")

# II. Lifespan Analysis
lifespans = [float(cat['life_span'].split(' - ')[0]) for cat in cats_data]
min_lifespan = min(lifespans)
max_lifespan = max(lifespans)
mean_lifespan = statistics.mean(lifespans)
median_lifespan = statistics.median(lifespans)
std_dev_lifespan = statistics.stdev(lifespans)

print(f"Lifespan (years) - Min: {min_lifespan}, Max: {max_lifespan}, Mean: {mean_lifespan}, Median: {median_lifespan}, Std Dev: {std_dev_lifespan}")

# III. Frequency Table of Country and Breed
from collections import defaultdict

country_breed_freq = defaultdict(list)
for cat in cats_data:
    country_breed_freq[cat['origin']].append(cat['name'])

for country, breeds in country_breed_freq.items():
    print(f"{country}: {len(breeds)} breeds")

# Task 3: Analyzing the Countries API
import requests

def get_countries_data(url):
    response = requests.get(url)
    return response.json()

countries_api = 'https://restcountries.com/v3.1/all'
countries_data = get_countries_data(countries_api)

# I. 10 Largest Countries by Area
largest_countries = sorted(countries_data, key=lambda x: x['area'], reverse=True)[:10]
print("10 Largest Countries by Area:")
for country in largest_countries:
    print(f"{country['name']['common']}: {country['area']} km²")

# II. 10 Most Spoken Languages
from collections import Counter

languages = [lang for country in countries_data for lang in country['languages'].values()]
most_spoken_languages = Counter(languages).most_common(10)
print("10 Most Spoken Languages:")
print(most_spoken_languages)

# III. Total Number of Languages
total_languages = len(set(languages))
print(f"Total Number of Languages: {total_languages}")

# Task 4: Reading UCI Machine Learning Repository
import requests
from bs4 import BeautifulSoup

def get_uci_datasets(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    datasets = soup.find_all('a', href=True)
    return [dataset.text for dataset in datasets if 'datasets' in dataset['href']]

uci_url = 'https://archive.ics.uci.edu/ml/datasets.php'
uci_datasets = get_uci_datasets(uci_url)
print(uci_datasets)

