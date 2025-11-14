#네이버 기사 크롤링(하위페이지)

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
driver.get("https://news.naver.com/section/101")  # 네이버 경제 뉴스

# 뉴스 기사 가져오기
news = driver.find_elements(By.CLASS_NAME, "_SECTION_HEADLINE")

for content in news[:2]:  # 상위 2개 뉴스만 가져오기
    title = content.find_element(By.CLASS_NAME, "sa_text_strong").text
    link = content.find_element(By.CLASS_NAME, "sa_text_title").get_attribute("href")  # 기사 URL 가져오기

    print(f"기사 제목: {title}")  # 기사 제목 출력
    print(f"기사 URL: {link}\n")  # 기사 URL 출력
    
    # 새 탭에서 열기
    driver.execute_script(f"window.open('{link}', '_blank');")
    time.sleep(2)

    # 새 탭으로 전환
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(3)

    # 기사 본문 가져오기
    try:
        article = driver.find_element(By.ID, "dic_area").text  # 기사 본문 찾기
        print(f"기사 본문: {article[:300]}...")  # 본문 일부 출력 (앞 300자)
    except:
        print("기사 본문을 찾을 수 없습니다.")

    # 새 탭 닫기
    driver.close()

    # 다시 원래 창으로 전환
    driver.switch_to.window(driver.window_handles[0])

# 드라이버 종료
driver.quit()
