# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:13:26 2025

@author: MYCOM
"""
#web크롤링 or 스크래핑
#특정 웹사이트에서 원하는 데이터를 자동으로 수집하는 기술
#뉴스기사, 주가, 제품정보, 가격비교 데이터 등을 쉽게 수집할 수 있다.

#파이썬 코드로 웹 요청하는 라이브러리
#pip install requests

#1. requests를 이용한 웹페이지 요청
import requests
url = "https://www.naver.com"
response = requests.get(url)
print(response)

#응답코드
print(response.status_code)
#2xx -> 정상응답
#3xx -> redirect(페이지 이동됨)
#4xx -> 클라이언트 오류(요청쪽 오류)
#5xx -> 서버오류(수신쪽 오류)

#응답본문
print(response.text[:200])
#페이지가 로딩된 후에 ajax로 화면을 동적으로 그리는 웹사이트라면
#ajax요청에 대한 데이터는 가져올 수 없다.


#2. requests를 이용해 파라미터 전송
url = "https://search.naver.com/search.naver"
#query=aaa
params = {
    "query" : "크롤링",
    "where" : "news",
    "sm" : "tab_jum",
    #search mode 기본모드?
}

response = requests.get(url,params)
"""
https://https://search.naver.com/search.naver
?query=크롤링&where=news&sm=tab_jum
"""
print(response.text[:500])

#3. requests를 이용해 post요청
url = "https://www.google.com"
response = requests.post(url)
print(response)

#4. 헤더 설정(차단 방지)
#봇이 아니라 크롬에서 보낸 것 처럼 위장
# navigator.userAgent
headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    
}
url = "https://www.google.com"
response = requests.get(url, headers=headers)
print(response.text)

