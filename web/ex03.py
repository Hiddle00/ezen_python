# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 12:12:46 2025

@author: MYCOM
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

#1. html요소 직접 접근
print(soup.title) #title태그
print(soup.title.text) #태그사이 텍스트
print(soup.title.name) #태그이름

#2. find()
#태그 기반으로 html요소를 찾고, 첫번째로 찾은 요소만 반환
h1 = soup.find("h1")
print(h1)
#news.naver.com에서 h1태그를 찾는다.(기본적으로 제일 위의 1개만)

print(soup.find("div"))

#3. find_all()
#태그 기반으로 html요소를 찾고, 모든 요소를 리스트로 반환
all_links_list = soup.find_all("a")
print(len(all_links_list))
for link in all_links_list[:10] :
    print(link)
    
#4. select()
#선택자 기반으로 html요소를 찾고, 모든 요소를 리스트로 반환
links = soup.select("a")
print(len(links))

#5. select_one()
#선택자 기반으로 html요소를 찾고, 첫번째 요소 반환
span = soup.select_one("span")
print(span)

#6. 요소에서 태그속성 가져오기
a_tag = soup.select_one("a")
print(a_tag)
#href속성
print(a_tag["href"])
#class
#속성을 안전하게 가져오기(get())
#dictionary처럼 []로 접근하면 속성이 없을경우 에러
print(a_tag.get("class"))

#7. 텍스트 가져오기(태그사이)
p = soup.select_one("p")
print(p)
print(p.text)
print(p.get_text())
