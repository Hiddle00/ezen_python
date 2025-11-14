# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 12:13:00 2025

@author: MYCOM
"""
#stock.csv 데이터 전처리
import pandas as pd
df = pd.read_csv("stock.csv", parse_dates=["date"])
#date컬럼은 날짜 타입으로 불러온다.
print(df.info())

#2018년 5월 4일에 삼성전자 액면분할
#1/50
#원래 1주당 500,000 -> 10,000 50주

#1970년 1월 1일 00시 00분 00초 : 시작 = 제일 작은값(0)

#액분 일자
split_date = pd.to_datetime("2018-05-03")
#df["date"] <= split_date : 가능
#df["date"] <= "2018-05-03" : 불가능

df.loc[df["date"] <= split_date, "close_price"] /= 50

df.to_csv("stock_proc.csv")

from sklearn.linear_model import LinearRegression
#단순 선형회귀를 이용한 주가예측

df["date_int"] = df["date"].map(pd.Timestamp.toordinal)
print(df.head())

#가로축 (입력값, 독립변수, 날짜정수)
X = df[["date_int"]]

#세로축 (출력값, 종속변수, 종가)
y = df["close_price"]

model = LinearRegression()
model.fit(X,y)

#739572 -> 11월 17일
print(df.tail())
model.predict([[739572]])

pred = model.predict(X)

import matplotlib.pyplot as plt
#실제 날짜에 따른 종가
plt.plot(df["date"], df["close_price"], color="blue")

#선형회귀 모델로 예측한 날짜에 따른 종가
plt.plot(df["date"], pred, color="red")

plt.show()