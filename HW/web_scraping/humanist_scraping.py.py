# Jacky, Braden, Arnav, Leo

# Step 0: Import libraries

from bs4 import BeautifulSoup
import requests

def scrape_screenplay(url):
    response = requests.get(url)
    html_string = response.text
    return html_string

# Step 1: Get data and generate content

content = scrape_screenplay("https://humanist.kdl.kcl.ac.uk/")

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

links = soup.find_all('a')
# print(links)

# Step 2: Put data into two lists and merge them into content

linkList = []
volumeList = []

for link in links:
    text = link.get_text().lower()
    if 'volume' in text:
        linkList.append("https://humanist.kdl.kcl.ac.uk" + link.get('href'))
        volumeList.append(text)

res = dict(zip(volumeList, linkList))

# For final formatting

# for key, value in res.items():
#     print(key, ':', value)

# Step 3: Calling the first url and save the text

temp = scrape_screenplay(url=res['volume 1 5/87-5/88'])
# print(temp)

soup_temp = BeautifulSoup(temp, "html.parser")
# print(soup_temp.prettify())

links_temp = soup_temp.find_all('a')
# print(links_temp)

linkT = []
volumeT = []

for link in links_temp:
    text = link.get_text().lower()
    if 'txt' in text:
        linkT.append("https://humanist.kdl.kcl.ac.uk/Archives/Virginia/v01/" + link.get('href'))
        volumeT.append(text)

resT = dict(zip(volumeT, linkT))

for key, value in resT.items():
    print(key, ':', value)