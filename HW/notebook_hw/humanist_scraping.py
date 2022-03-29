# Jacky, Braden, Arnav, Leo

# Step 0: Import libraries

from bs4 import BeautifulSoup
import requests
import json

def scrape_webpage(url): #rename function to be more meaningful
    response = requests.get(url)
    html_string = response.text
    return html_string

# Step 1: Create a function for getting the urls wuth title

#lowercase and underscores are the normal convention for naming functions in Python. Camelcasing like you had is more normal in JavaScript or for classes.
def get_content(url='', keyword='', url_head="https://humanist.kdl.kcl.ac.uk", filename=''):
    content = scrape_webpage(url)
    soup = BeautifulSoup(content, "html.parser")
    links = soup.find_all('a')

    # linkList = []
    # volumeList = [] #Save yourself having to zip your lists by just creating your dictionary from the ouset
    result = {} #Create a dictionary to store the results, and give a more descriptive name to the variable
    for link in links:
        text = link.get_text().lower()
        if keyword in text:
            result[text] = url_head + link.get('href')
            # linkList.append(url_head + link.get('href'))
            # volumeList.append(text)

    # res = dict(zip(volumeList, linkList))

    # Saving into new py doc

    # with open(filename, 'w') as file:
    #     file.write(json.dumps(result, indent=2))

    return result

res = get_content(
    url="https://humanist.kdl.kcl.ac.uk/",
    keyword="volume",
    filename="main_page.txt")

print("Printing the main page:\n")
for key, value in res.items():
    print(key, ':', value)

# Step 2: Calling two url and save the text

res_v1 = get_content(
    url=res['volume 1 5/87-5/88'],
    keyword="txt",
    url_head="https://humanist.kdl.kcl.ac.uk/Archives/Virginia/v01/",
    filename="1st_volume.txt")

res_v33 = get_content(
    url=res['volume 33'],
    keyword="humanist",
    filename="33rd_volume.txt")

# print("\nPrinting the 1st volume:\n")
# for key, value in res_v1.items():
#     print(key, ':', value)

# print("\nPrinting the 33rd volume:\n")
# for key, value in res_v33.items():
#     print(key, ':', value)

# Parse the text in each link

count = 0
final = {}

for key, value in res_v1.items():
    content = scrape_webpage(value)
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()
    with open('text_1st_volume.txt', 'w') as file:
        file.write(text)

    # too long need to break
    count += 1
    if count == 1: break

# print(final)