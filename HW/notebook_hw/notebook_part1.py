"""
The goal: take the data from the plain text files and save it to a dataframe in Pandas.

1. We need to get metadata and data for the websites.
2. We need to store the data to the dataframe.

Finally, so we don't have to web scrape every time, try using the following code:
humanist_vols.to_csv('web_scraped_humanist_listserv.csv')
What does this do to our data? You can read about the to_csv() method here 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv.

"""

from humanist_scraping import res_v1, scrape_webpage
from bs4 import BeautifulSoup
import pandas as pd

# print("\nPrinting the 1st volume:\n")
# for key, value in res_v1.items():
#     print(key, ':', value)

count = 0
final = []

for key, value in res_v1.items():
    content = scrape_webpage(value)
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()[:10]
    # with open('text_1st_volume.txt', 'w') as file:
    #     file.write(text)
    # final[key] = text
    final_dict = {}
    final_dict["key"] = key
    final_dict["value"] = text
    final.append(final_dict)

df = pd.DataFrame(final)
print(df)