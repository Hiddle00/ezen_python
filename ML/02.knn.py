import warnings
warnings.filterwarnings("ignore")
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 15:16:28 2025

@author: MYCOM
"""

# KNN (최근접 이웃 알고리즘 / nearest neighbors)을 이용한 분류

#pip install mglearn
import mglearn
import matplotlib.pyplot as plt


# 최근접 이웃 분류(지도학습의 분류문제)
mglearn.plots.plot_knn_classification(n_neighbors=1)
mglearn.plots.plot_knn_classification(n_neighbors=2)
mglearn.plots.plot_knn_classification(n_neighbors=3)

# 최근접 이웃 회귀(지도학습의 회귀문제)
mglearn.plots.plot_knn_regression(n_neighbors=1)
mglearn.plots.plot_knn_regression(n_neighbors=2)
mglearn.plots.plot_knn_regression(n_neighbors=3)

plt.show()

import pandas as pd
#남여 성별데이터를 읽어 들인다.
df = pd.read_csv("gender.csv")
print(df.head())
print("=" * 30)

# 독립변수(X)와 종속변수(y)로 나눈다.
# 독립변수 : 키, 몸무게
# 종속변수 : 성별
X = df[["키", "몸무게"]]
y = df[["성별"]]
print(X)
print(y)
print("-" * 30)


# KNN학습 ( KNeighborsClassifier 객체 - 분류?)
from sklearn.neighbors import KNeighborsClassifier
# n_neighbors : 이웃 갯수
knn = KNeighborsClassifier(n_neighbors = 3)

# 독립변수와 종속변수를 이용해서 학습한다.
knn.fit(X,y)

# 자기가 학습한 데이터를 예측해 본다.
y_pred = knn.predict(X)
print(y_pred)

# score()함수를 이용해서 정확도를 측정한다.
print("정확도 => %.2f " % knn.score(X,y))

# 남, 여 각각의 데이터에 대해서 예측해본다.
XX = [[176, 76], [156, 41]]
y_pred = knn.predict(XX)
print(y_pred)

gender = ["여성", "남성"]
for item in y_pred :
    #print("성별 ==>" + str(item))
    print("성별==> " + gender[item])





#==========================================
# 최근접 이웃 회귀를 이용한 주가예측
# 삼성전자(005930) 주가 예측

df = pd.read_csv("005930.csv")
print(df.head())
print("=" * 30)

# 특정일 이후의 데이터만 추출한다.
cutDate = "2019.12.20"
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
# 총 202개 데이터를 7:3으로 나눈다
from sklearn.model_selection import train_test_split

# 각각을 훈련 데이터와 테스트 데이터로 분리한다.
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print("=" * 30)

# 최근접 이웃 회귀 알고리즘을 동작한다.
# KNN 학습 ( KNeighborsRegressor 객체 )
from sklearn.neighbors import KNeighborsRegressor

reg = KNeighborsRegressor(n_neighbors = 100)

# 훈련 데이터로 학습한다
reg.fit(X_train, y_train)

# 테스트 데이터로 정확도를 측정해본다.
print("정확도 => %.2f " % reg.score(X_test,y_test))
# 0.99 overfit 과적합. 학습데이터에 과하게 편중된 학습결과

# 오늘의 시가를 이용해서 종가를 예측해 본다.
begin = [[ 106900 ]]
y_pred = reg.predict( begin )
end = int(y_pred[0]) # 예측가격을 정수로 변환
print(f"예측종가 : {end}")




