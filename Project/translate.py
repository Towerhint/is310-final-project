# Basic APIs
import requests
from bs4 import BeautifulSoup
import json

# Google APIs
from googletrans import Translator

# detect the input language

translator = Translator()  # Create a Translator instance to use the API

def detect(string):
    result = translator.detect(string)
    return result

def translate(dest, string):
    result = translator.translate(string, dest=dest)
    return result

# testing detect

# print(detect('이 문장은 한글로 쓰여졌습니다.'))
# print(detect('Tiu frazo estas skribita en Esperanto.'))
# print(detect('你好'))
# print(detect("bravo"))  # Some words may be ambiguous
