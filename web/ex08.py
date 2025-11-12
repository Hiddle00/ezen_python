# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 09:11:06 2025

@author: MYCOM
"""
#잡코리아 채용공고 크롤링
import requests
from bs4 import BeautifulSoup
url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
#print(response.text[:500])

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.find("title"))

#채용공고 테이블의 tr가져오기
#soup.find_all("tr", class_="devloopArea")
jobs = soup.select("tr.devloopArea")
print(len(jobs))
#print(jobs[0])

#채용회사 이름
comp_name = jobs[0].select_one("td.tplCo > a").text
print(comp_name)
#공고 제목
info = jobs[0].select_one("td.tplTit a").text
print(info)
#근무 조건
etcs = jobs[0].select_one("td.tplTit p.etc").text
print(etcs)
#부가설명
dsc = jobs[0].select_one("td.tplTit p.dsc").text
print(dsc)

#잘라서 배열로 변환
dsc_list = []
dsc_list = dsc.split(",")
print(dsc_list)
etc_list = etcs.split("\n")
print(etc_list)

#빈문자열 원소 제거
etcs = [etc for etc in etc_list if etc != '']
print(etcs)

for job in jobs[:40] :
    company = job.select_one("td.tplCo > a").text
    title = job.select_one("td.tplTit a").text
    print("회사 :", company)
    print("제목 :", title)
