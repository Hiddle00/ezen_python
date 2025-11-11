# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 10:35:11 2025

@author: MYCOM
"""
#네이버 증권에서 삼전 주가 가져오기
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/item/main.naver?code=005930"

response = requests.get(url)
#print(response.text[:200])

soup = BeautifulSoup(response.text, "html.parser")
div = soup.select_one("div#rate_info_krx")
#soup.find("div", id="rate_info_krx")
#div 중 아이디가 rate_info_krx인 요소 하나를 찾는다.
#print(div)

today = div.select_one(".today > .no_today > .no_up > .blind")
print("현재 가격 :", today.text)

rows = div.select("table > tr")
#print(table)
for row in rows :
    cols = row.find_all("td")
    # =============================================================================
    stock = [ col.find("span", class_="blind").text for col in cols]
    print(stock)
    # =============================================================================
    for col in cols :
        print(col.find("span").text)
        print(col.find("span", class_="blind").text)
    #print(col[0].find("span", class_="blind").text)
print(stock)
l = []
for i in range(1, 6) :
    l.append(i)
print(l)
# ->
k = [ i for i in range(1, 6)]
print(k)