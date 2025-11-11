# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 11:38:05 2025

@author: MYCOM
"""
#네이버 뉴스 기사 제목 + 링크 가져오기
import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/104"
#네이버뉴스(세계) 홈페이지

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#print(soup.prettify())

newsct = soup.find("div", id="newsct")
#print(newsct)

ul = newsct.select_one("div > ul")
#print(ul)
li = ul.select("li")
print(len(li))
#soup.select("#newsct > div > div > ul > li")

for news in li :
    #news -> li[0] ~ li[9]
    link = news.select_one("div > div > div.sa_text > a")
    link.get("href")
    title = link.select_one("strong")
    print("링크 :", link.get("href"))
    print("제목 :", title.text)