# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 14:13:55 2025

@author: MYCOM

data = [11, 22, 33, 44, 55]

idx = 0
for v in data :
    print(f"{idx} => {v}")
    idx += 1

print("--" * 20)
for idx, v in enumerate(data) :
    print(idx, "->", v)


x = 10
y = 22.3
print("정수값 : %d, 실수값 : %f" % (x, y))
"""
# OLS (최소자승법)을 이용한 주가 예측
# Ordinary Least Square
import warnings
warnings.filterwarnings("ignore")
import pandas as pd

# 삼성전자(005930) 주가 예측
df = pd.read_csv("005930.csv")
print(df.head())
print("=" * 30)

# 특정일 이후의 데이터만 추출한다.
cutDate = "2024.01.01"
df =  df.loc[ df["날짜"] >= cutDate]
print(df.tail)
print("=" * 30)

# 독립변수(X)와 종속변수(y)로 나눈다.
# 독립변수 : 시가
# 종속변수 : 종가
X = df[["시가"]]
y = df[["종가"]]
print(X)
print(y)
print("=" * 30)

# 독립변수(X)와 종속 변수(y)를 각각 
# 훈련 데이터와 테스트 데이터로 분리한다.
# 총 450여의 데이터를 7:3으로 나눈다
from sklearn.model_selection import train_test_split

# 각각을 훈련 데이터와 테스트 데이터로 분리한다.
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state= 2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print("=" * 30)

import statsmodels.api as sm
import statsmodels.formula.api as smf

model = sm.OLS(X_train, y_train)
result = model.fit()

# 테스트데이터로 정확도를 수동측정
y_pred = result.predict(X_test)
count = 0 # 일치하는 갯수
for idx, v in enumerate(y_test) :
    if v == int(y_pred.iloc[idx]) :
        count = count + 1
score = count / len(y_test) * 100
print(f"정확도 : {score}")


# 오늘의 시가를 이용해서 종가를 예측해 본다.
begin = [[ 106900 ]]
y_pred = result.predict( begin )
end = int(y_pred[0]) # 예측가격을 정수로 변환
print(f"예측종가 : {end}")






