import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_stock_data(stock_code, pages=2):
    stock_data = []
    for page in range(1, pages + 1):
        url = f"https://finance.naver.com/item/sise_day.nhn?code={stock_code}&page={page}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", class_="type2")
        rows = table.find_all("tr")

        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) < 7:  # 빈 행 제외
                continue
            date = cols[0].get_text(strip=True)
            close_price = cols[1].get_text(strip=True).replace(',', '')  # 종가
            volume = cols[6].get_text(strip=True).replace(',', '')  # 거래량
            if close_price and volume:
                stock_data.append({"date": date, "close_price": int(close_price), "volume": int(volume)})
    
    return stock_data

# 삼성전자 (005930) 주식 데이터 크롤링
stock_code = "005930"  # 삼성전자
pages = 500  # 최근 5페이지 데이터 수집
stock_data = get_stock_data(stock_code, pages)

# 데이터프레임 변환
df = pd.DataFrame(stock_data)
#날짜형태로 변환
df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by="date", ascending=True)
print(df.head())
df.to_csv("stock.csv")
print(df.tail())