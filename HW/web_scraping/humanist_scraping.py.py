# Jacky, Braden, Arnav, Leo

# Step 0: Import libraries

from bs4 import BeautifulSoup
import requests
import json

def scrape_screenplay(url):
    response = requests.get(url)
    html_string = response.text
    return html_string

# Step 1: Create a function for getting the urls wuth title

def getContent(url='', keyword='', url_head="https://humanist.kdl.kcl.ac.uk", filename=''):
    content = scrape_screenplay(url)
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('a')

    linkList = []
    volumeList = []

    for link in links:
        text = link.get_text().lower()
        if keyword in text:
            linkList.append(url_head + link.get('href'))
            volumeList.append(text)

    res = dict(zip(volumeList, linkList))

    # Saving into new py doc

    with open(filename, 'w') as file:
        file.write(json.dumps(res, indent=2))

    return res

res = getContent(
    url="https://humanist.kdl.kcl.ac.uk/",
    keyword="volume",
    filename="main_page.txt")

print("Printing the main page:\n")
for key, value in res.items():
    print(key, ':', value)

# Step 2: Calling two url and save the text

res_v1 = getContent(
    url=res['volume 1 5/87-5/88'],
    keyword="txt",
    url_head="https://humanist.kdl.kcl.ac.uk/Archives/Virginia/v01/",
    filename="1st_volume.txt")

res_v33 = getContent(
    url=res['volume 33'],
    keyword="humanist",
    filename="33rd_volume.txt")

print("\nPrinting the 1st volume:\n")
for key, value in res_v1.items():
    print(key, ':', value)

print("\nPrinting the 33rd volume:\n")
for key, value in res_v33.items():
    print(key, ':', value)

