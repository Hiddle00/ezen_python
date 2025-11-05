# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 14:58:11 2025

@author: MYCOM
"""

# 로지스틱회귀(LogisticRegression) 분석 (이진분류기)

import warnings
warnings.filterwarnings("ignore")
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


# 로지스틱 회귀로 학습 ( KNeighborsClassifier 객체 - 분류?)
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(X,y)

# 남,여 각각의 데이터에 대해서
# 예측해 본다.
XX = [[176, 76], [156, 41]]
y_pred = lr.predict( XX )
print(y_pred)