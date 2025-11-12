import subprocess
#main과 sub가 나뉜다. 이게 있어야 크롬 브라우저에 대한 정보를 가져옴
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_browser = subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')
#경로에 있는 쿠키를 읽어온다
options = Options()
#브라우저에 요청을 보낼때 헤더에 포함할 인수
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
#보안 / 크롬의 기본적인 보안을 비활성화
options.add_argument('--no-sandbox')
#메모리 사용량 옵션
options.add_argument('--disable-dev-shm-usage')
#https 인증 무시
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#우회하기 위한 옵션헤더?
driver = webdriver.Chrome(options=options)
#service=Service(ChromeDriverManager().install()), 
driver.get("https://www.google.com")
time.sleep(2)

# 검색창 찾기
search_box = driver.find_element(By.NAME, "q")

# 검색어 입력 후 엔터
search_box.send_keys("Python Selenium")
search_box.send_keys(Keys.RETURN)

time.sleep(2)
# =============================================================================
# 
# # 검색 결과 가져오기
# titles = driver.find_elements(By.TAG_NAME, "h3")
# print(titles)
# for title in titles[:5]:
#     print(title.text)
# =============================================================================
#검색 결과 가져오기
#검색 타이틀만 조회
tis = driver.find_elements(By.TAG_NAME, "h3")
#print(len(tis))
for title in tis :
    print(title.text)
    
tis[0].click()


