# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 12:12:40 2025

@author: MYCOM
"""
#네이버 뉴스 크롤링 및 데이터프레임 변환
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
# =============================================================================
import re
# =============================================================================
#1. 네이버 뉴스 페이지 크롤링
url = "https://news.naver.com/section/105"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

#뉴스 기사 제목, 링크 크롤링
titles = soup.select("div.sa_text > a")
news_data = []
for title in titles :
    news_title = title.text.strip()
    news_link = title.get("href").strip()
    print("제목 :", news_title)
    print("링크 :", news_link)
    
    #3. 뉴스 기사 본문 크롤링
    article_response = requests.get(news_link)
    article_soup = BeautifulSoup(article_response.text, "html.parser")
    article = article_soup.select_one("article")
    #print("내용 :", article.text[:200])
    print("--" * 25, "\n")
    
    # =============================================================================
    article_text = article.text.replace("\t", "").replace("\n", "")
    article_text = re.sub(" +", " ", article_text)
    #re.sub("a+")
    #a문자가 하나 이상인것
    # =============================================================================

    news_dict = {
        "제목" : news_title,
        "링크" : news_link,
        "내용" : article_text
    }
    news_data.append(news_dict)
    
    time.sleep(2)
    
    """
    [
     {
      title : "뉴스제목",
      link : "링크",
      content : "내용"
     },
     {
      title : "뉴스제목",
      link : "링크",
      content : "내용"
     }
    ]
    """
#print(news_data)

#4. csv 저장
df = pd.DataFrame(news_data)
df.to_csv("naver_news_data.csv")