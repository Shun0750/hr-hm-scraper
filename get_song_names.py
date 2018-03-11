# -*- coding: utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
import re

url = 'http://hvymetal.com/'
html = sys.argv[1]
url = url + html

r = requests.get(url)
content_type_encoding = r.encoding if r.encoding != 'ISO-8859-1' else None
soup = BeautifulSoup(r.content, 'html.parser', from_encoding=content_type_encoding)

termlist = soup.find(id="termlist")
print("START========")

for list in termlist.find_all('a'):
    inner_text = list.text.replace('\n','')
    if (len(inner_text) > 0 and u'項目' not in inner_text) and (len(inner_text) > 0 and u'お気に入り' not in inner_text):
       print(inner_text)
