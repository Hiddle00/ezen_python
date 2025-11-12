# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 10:11:55 2025

@author: MYCOM
"""
#다나와 제품 크롤링
import requests
from bs4 import BeautifulSoup
url = "https://prod.danawa.com/list/?cate=112758&15main_11_02"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
#print(response) 200응답
#print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

prodlist = soup.select_one("div.main_prodlist")
#print(len(prodlist) select를 했을때 1개의 요소를 잘 찾았는지 확인하면 좋음

items = prodlist.select("ul > li.prod_item")
print(len(items))
item = items[0].select_one("div > div.prod_info a")
name = item.text.strip()
#strip() : 양쪽 공백 제거
#" 안 녕 ".strip() : "안 녕"
link = item.get("href")
print(name, link)

price = items[0].select_one("div > div.prod_pricelist li.rank_one > p.price_sect strong").text.strip()
print(price)

names = []
prices = []
for item in items :
    item = item.select_one("div > div.prod_info a")




