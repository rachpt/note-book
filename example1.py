# coding: UTF-8

import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)

with open('title.txt', "a+") as f:
    f.write(title)
    f.close()
