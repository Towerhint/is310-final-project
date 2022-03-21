import requests
from bs4 import BeautifulSoup

file = open('raw_script_urls.txt')
for item in file:
    print(item)