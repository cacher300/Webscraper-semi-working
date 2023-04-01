import requests
from bs4 import BeautifulSoup

# Make a GET request to the webpage
source = requests.get('http://www.hockeychallengepicks.ca/').text

soup = BeautifulSoup(source, 'lxml')

# Find all the table tags on the webpage
tables = soup.find_all('table')

# Loop over each table and extract the links
for table in tables:
    links = table.find_all('a')
    for link in links:
        print(link.text)
