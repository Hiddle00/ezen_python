# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 09:08:43 2025

@author: MYCOM
"""
#셀레니움에서 자바스크립트 코드 실행하기
from selenium import webdriver

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


driver = webdriver.Chrome(options=options)
#service=Service(ChromeDriverManager().install()), 

#driver.get("https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0&vertical=search")
driver.get("https://coupang.com")
time.sleep(2)
#웹 페이지가 변하면 객체가 가진 값도 변함
#브라우저를 실행하는 라이브러리이기 때문에

#자바스크립트 코드 실행
#driver.execute_script("alert('경고!')")

#무한 스크롤 처리
#1. 스크롤 높이 구하기
#2. 현재 스크롤 위치를 스크롤 높이로 이동
#3. (데이터 로딩 대기)
#4. 스크롤 높이 다시 구하기
#5. 현재 스크롤 위치와 최대 스크롤 높이가 같으면 중지, 그렇지 않으면 반복

height = driver.execute_script("return document.body.scrollHeight")
#기본적으로 반환값을 돌려받지 못함
#return으로 돌려받음
while True :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if height == new_height :
        break;
    height = new_height
    
