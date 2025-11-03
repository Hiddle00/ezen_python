# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 14:43:35 2025

@author: MYCOM
"""
#hyperParameter
#LinearRegression (선형 회귀 분석)을 이용한 주가 예측
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

# 선형 회귀모델을 이용하여 주가를 예측한다.
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
#copy_X= : 입력 데이터의 복사 여부
#fit_intercept= : 절편의 값을 계산 여부
#normalize= : 정규화여부
#n_jobs= : 데이터 분석에 사용할 코어의 갯수(기본값은 1. -1을 입력하는 경우 사용가능한 모든 코어를 사용)

# 훈련 데이터로 학습한다
lr.fit(X_train, y_train)

# 테스트 데이터로 정확도를 측정해본다.
print("정확도 => %.2f " % lr.score(X_test,y_test))
# 0.99 overfit 과적합. 학습데이터에 과하게 편중된 학습결과

# 오늘의 시가를 이용해서 종가를 예측해 본다.
begin = [[ 106900 ]]
y_pred = lr.predict( begin )
end = int(y_pred[0]) # 예측가격을 정수로 변환
print(f"예측종가 : {end}")