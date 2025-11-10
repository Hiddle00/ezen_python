# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:57:02 2025

@author: MYCOM
"""
#beautifulSoup response 해석 라이브러리
#BS를 이용한 html 데이터 추출
#bs는 HTML과 XML데이터를 파싱하여 원하는 데이터를 쉽게 추출하는 라이브러리
# pip install beautifulsoup4
#텍스트를 태그형태로 분석, 해석
"""
<div id="a">
    <div id="b"></div>
</div>
"""

from bs4 import BeautifulSoup
import requests

url = "https://news.naver.com"
headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    
}


response = requests.get(url, headers=headers)
#print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser")
print(soup)
print(soup.title)
print(soup.title.text)
print(soup.a)
print(soup.prettify())
#들여쓰기