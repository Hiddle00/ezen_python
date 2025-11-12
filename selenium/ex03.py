# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 12:20:06 2025

@author: MYCOM
"""
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
driver.get("https://www.google.com")
#time.sleep(1)

#login = driver.find_element(By.XPATH, '//*[@id="gb"]/div[3]/a')
#html 하위의(//)
#어떤 태그던지 상관없이(*)
#id속성의 값이 gb인 요소([@id="gb"])
#의 div자식중 3번째(/div[3])
#의 자식 a (/a)
#XPATH

#login.click()

#sleep이 안전하지 않은경우
#WebDriverWait
#html의 특정 태그가 특정 상태가 될 때까지 최대 지어된 시간만큼 대기
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#WebDriverWait(driver, 시간).until(조건)

login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gb"]/div[3]/a')))
#구글 로그인 a태그가 클릭 가능할 때 까지 대기(최대 10초)
#지정된 시간이 넘어가면 예외 발생

#종류가 많다 ex선택가능, 클릭가능, 

login.click()