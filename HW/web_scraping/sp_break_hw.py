import requests
from bs4 import BeautifulSoup
import json

# Extract all the files 

file = open('/Users/fafnir/Documents/GitHub/is310_final_project/HW/web_scraping/raw_script_urls.txt', 'r')  # Note that the path may need some changes(may add pathlib in the future)
url = []
for item in file:
    parts = item.split(' +++$+++ ')
    url.append((parts[1].strip(), parts[2].strip()))

# Use web-scraping to get all data and save them in a single file
# There are 617 urls, to save time, we only scrape the first 50...

# Request the pages

def getText(url):
    response = requests.get(url=url)
    response.raise_for_status()
    return response.text

# We need to get the body from these texts

final = {}

for item in url[0:50]:
    text = getText(item[1])
    document = BeautifulSoup(text, "html.parser")
    final[item[0]] = str(document)

with open('result.json', 'w') as file:
        file.write(json.dumps(final, indent=2))