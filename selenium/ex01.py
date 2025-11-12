# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 11:18:22 2025

@author: MYCOM
"""
#selenium을 이용한 웹 자동화
"""
selenium은 웹 브라우저를 조작하는 라이브러리로,
실제 브라우저를 조작하여 웹페이지에서 버튼을 클릭하거나, 스크롤을 내리거나, 
키보드를 입력하는 등의 작업을 자동화 할 수 있다.
"""
#옛날에는 크롬 드라이버를 설치해야 했다. chromeDriver.exe
#현재는 라이브러리를 설치하면 자동 설치된다.

#pip install selenium
#pip install webdriver-manager

from selenium import webdriver

#크롬 드라이버 실행
driver = webdriver.Chrome()

#google.com을 크롬드라이버로 연다.
driver.get("https://google.com")

#브라우저에서 title태그의 값을 꺼낸다.
print(driver.title)

#브라우저 닫기
#driver.quit()

#태그를 찾기 위해 필요한 클래스
from selenium.webdriver.common.by import By
#키보드 입력을 위해 필요한 클래스
from selenium.webdriver.common.keys import Keys

#selenium으로 웹 요소 찾고, 조작하기
#1. 검색창 찾기
search_box = driver.find_element(By.NAME, "q")
#document.getElementsByName("q")[0]
#2. 검색창 클릭 : auto포커스가 아닌곳에선 필요
#3. 검색창에 "python"입력
search_box.send_keys("python")
#4. 엔터키 입력
search_box.send_keys(Keys.RETURN)

#find_element(s)
#크롬 드라이버가 연 페이지에서 html요소를 찾기
#find_element(By.속성, "값")
#

#By
#By.NAME : name속성
#find_element(By.NAME, "q")
#name속성의 값이 q인 html요소 하나

#By.ID : id속성
#find_element(By.ID, "a")
#id속성의 값이 a인 html요소

#By.CLASS_NAME : class속성
#By.TAG_NAME : 태그이름
#By.CSS_SELECTOR : css셀렉터

#send_keys
#find_element로 찾은 html요소에 키보드 입력
#send_keys("키보드입력값")

#Keys
#Keys.ENTER : enter키
#Keys.RETURN : enter키
#Keys.ALT : alt키
#Keys.CONTROL : Ctrl키


