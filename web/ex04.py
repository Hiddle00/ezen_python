# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 09:15:48 2025

@author: MYCOM
"""
# 크롤링 단계
# 1. 크롤링 하고자하는 웹페이지에 HTTP요청
import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com"
#네이버뉴스 홈페이지
url = "https://news.naver.com/section/104"
#네이버뉴스(정치) 홈페이지

response = requests.get(url)
#네이버뉴스 홈페이지에 HTTP 요청
#요청이 잘못되면 400번대 응답이 "내려온다".
print(response)
print(response.status_code)
print(response.text[:500])  #네이버뉴스 홈페이지 HTML태그 문자열
#print(response.json())
#요청했을때 화면이아니라 데이터를 주는경우 json으로 받을 수 있다
#일반적인 평문, 텍스트라면 text로 


# 2. 웹페이지 텍스트를 구조화
#HTML처럼 태그 기반으로 DOM트리와 비슷한 객체구조
soup = BeautifulSoup(response.text, "html.parser")
#HTML이나 XML을 파싱하기 좋은 라이브러리
#클래스의 생성자 호출 / 파서 : 해석자?
#print(soup)


# 2.5 어떤 정보가 필요한지 브라우저에서 확인 > 구조를 파악

# 3. 구조화된 HTML 텍스트에서 원하는 정보를 해석(파싱)
print("--" * 25)
# =============================================================================
print(soup.title)
#bs의 html요소 가져오기 방법 여러가지
#1. find() : 첫번째로 찾은 요소 반환 / 태그 기반
a = soup.find("a", class_="a")
# a태그 중 클래스가 "a"인 요소 하나를 찾는다.
print(a)
a = soup.find("a", class_="ct_lnb_side_link")
print(a)
#리액트를 사용하면 css의 클래스를 동적으로 변환시키기 때문에 그때그때 찾아야 할 수도

#2. find_all() : 모든 요소 반환
a = soup.find_all("a")
print(len(a))
print(a[:3])

#3. select() / css 선택자 기반 동작
a = soup.select("a")
a = soup.select(".sa_list > li")
print(len(a))

#4. select_one()
headline = soup.select_one("#_SECTION_HEADLINE_LIST_0ylje")
print(headline)

# select_one이나 find는 요소를 찾지 못하면 None을 반환
# select, find_all은 요소를 찾지 못하면 빈 배열을 반환
# =============================================================================

#5. 찾은 요소에서 속성, 내용 꺼내기
a = soup.find("a")
print(a.text)  # .text : 태그사이의 텍스트
print(a.get_text())  # get함수로 꺼내기

# a의 속성 값 꺼내기
print(a["href"])  # href 값 꺼내기
#print(a["id"]) # 해당 속성이 없으면 에러

print(a.get("href"))
print(a.get("class")) # get으로 꺼내면 안전하게 처리
print("--" * 25)

br = soup.find("br")
print(br)
print(br.text)
print(br.get_text())


# 6. 부모요소찾기
print(a.parent)  # a태그의 부모요소

# 7. 자식요소찾기
header = soup.find("header")
#print(header)
a = header.find_all("a")
#해당하는 자손을 모두 찾음
a = header.find_all("a", recursive=False)
#recursive파라미터가 false면 직계자식만 찾는다.  /  $("header > a")
print(a)

a = soup.select("header a")
print(a)

# 8. 형제찾기
print(header.next_sibling.next_sibling)
#header태그의 다음 형제를 찾는다.
#줄바꿈이 있으면 빈 공백을 찾는다.
#다음이나 이전 형제가 줄바꿈(\n)인경우 한번 더 찾아야함.

print(header.previous_sibling.previous_sibling)
#header태그의 이전 형제
















