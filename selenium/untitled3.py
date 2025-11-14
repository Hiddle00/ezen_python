# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 11:30:57 2025

@author: MYCOM
"""
#네이버 로그인 자동화
import subprocess

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_browser = subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options)
url = "https://nid.naver.com/nidlogin.login"
driver.get(url)

#아이디 입력창 찾기
id = driver.find_element(By.ID, "id")
#id.send_keys("아이디")

#비밀번호 입력창 찾기
pw = driver.find_element(By.ID, "pw")
#pw.send_keys("비밀번호")

#로그인 버튼 찾기
btn = driver.find_element(By.ID, "log.login")
#btn.click()

#복사 붙여넣기를 지원하는 라이브러리를 설치
#pip install pyperclip

# =============================================================================
import pyperclip
#클립보드에 텍스트 복사
pyperclip.copy("테스트!")
#붙여넣기
text = pyperclip.paste()
print(text)
# =============================================================================

id = driver.find_element(By.ID, "id")
id.click()
pyperclip.copy("아이디")

# =============================================================================
from selenium.webdriver import ActionChains
# =============================================================================
#여러 키, 마우스 입력을 한번에 체이닝(묶어서) 처리하는 코드
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

pw = driver.find_element(By.ID, "pw")
pw.click()
pyperclip.copy("비밀번호")

action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

driver.find_element(By.ID, "log.login").click()




