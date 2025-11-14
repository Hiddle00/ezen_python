# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 10:05:18 2025

@author: MYCOM
"""
#네이버 기사 크롤링(하위페이지)
url = "https://news.naver.com/section/105"
import subprocess

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_browser = subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)
time.sleep(2)

#news = driver.find_element(By.ID, "newsct")
#news.find_element(By.TAG_NAME, "div")

news = driver.find_elements(By.CSS_SELECTOR, "#newsct > div ul > li")
print(len(news))

for content in news[:2] :
    #content > news[0] ~ news[1]
    title = content.find_element(By.CSS_SELECTOR, "a.sa_text_title")
    link = title.get_attribute("href")
    print("제목 :", title.text)
    print("링크 :", link)
    #a태그 클릭
    #title.click()
    
    #a태그의 링크를 구해서 새탭으로 열기
    #article = driver.find_element(By.TAG_NAME, "article")
    #print(article)
    #window.open("링크", "_blank) JS의 새탭에서 열기
    driver.execute_script(f"window.open('{link}');")
    time.sleep(1)
    #driver.execute_script(f"window.open('{link}', '_blank')")
    #뉴스 링크를 새탭에서 열기
    #셀레니움에서 새 탭을 열면 포커스가 새 탭으로 이동
    
    #새 탭으로 driver를 전환
    #탭 : naver,google,daum
    #   0번탭, 1번탭, 2번탭
    driver.switch_to.window(driver.window_handles[1])
    #1번탭으로 전환
    time.sleep(3)
    
    article = driver.find_element(By.TAG_NAME, "article")
    print("내용 :", article.text)
    
    # 새 탭 닫기
    driver.close()

    # 다시 원래 창으로 전환
    driver.switch_to.window(driver.window_handles[0])
    
    
#driver.quit()