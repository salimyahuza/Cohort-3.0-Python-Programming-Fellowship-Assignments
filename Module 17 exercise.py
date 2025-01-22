# Extracting the Table from UCI Machine Learning Repository and changing it to a json file
import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
table = soup.find('table', {'border': '1'})
headers = [header.text for header in table.find_all('th')]
rows = table.find_all('tr')[1:]

data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) == len(headers):
        data.append({headers[i]: cells[i].text.strip() for i in range(len(headers))})

# Save the data as a JSON file
with open('uci_datasets.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been scraped and saved to uci_datasets.json")


# Scraping the Presidents Table from Wikipedia
import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the presidents table
table = soup.find('table', {'class': 'wikitable'})
headers = [header.text.strip() for header in table.find_all('th')]
rows = table.find_all('tr')[1:]

data = []
for row in rows:
    cells = row.find_all(['th', 'td'])
    if len(cells) == len(headers):
        data.append({headers[i]: cells[i].text.strip() for i in range(len(headers))})

# Save the data as a JSON file
with open('us_presidents.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been scraped and saved to us_presidents.json")

