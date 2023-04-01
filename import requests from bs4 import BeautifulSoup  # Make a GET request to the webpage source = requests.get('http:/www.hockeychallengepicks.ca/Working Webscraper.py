import os
from bs4 import BeautifulSoup

# Get the path of the HTML file
html_path = os.path.join(os.getcwd(), 'data.html')

# Read the contents of the HTML file
with open(html_path, 'r') as f:
    html_content = f.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the table tags in the HTML content
tables = soup.find_all('table')

# Loop over each table and extract the info from the first column
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            print(cells[1].text)
