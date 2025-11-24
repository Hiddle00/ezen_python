# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 15:31:15 2025

@author: MYCOM
"""
#랜덤 포레스트 알고리즘
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np

iris_df = pd.read_csv("iris_encode.csv")
print(iris_df.head())
print("--" * 25)

#독립변수 : sepal_length, sepal_width, petal_length, petal_width
#종속변수 : species

X = iris_df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
print(X)
print("--" * 25)
y = iris_df["species"]
print(y)
print(np.unique(y))
print("--" * 25)

# 총 150개 데이터를 7:3으로 나눈다
from sklearn.model_selection import train_test_split

# 독립변수(X)와 종속 변수(y)를 각각 
# 훈련 데이터와 테스트 데이터로 분리한다.
# train_test_split() 기본적으로 75% : 25%
# test_size : 테스트 데이터셋의 비율(float)이나 갯수(int) (default = 0.25)
# train_size : 학습 데이터셋의 비율(float)이나 갯수(int) (default = test_size의 나머지)
# random_state : 데이터 분할시 셔플이 이루어지는데 이를 위한 시드값 (int나 RandomState로 입력)
# shuffle : 셔플여부설정 (default = True)

# 각각을 훈련 데이터와 테스트 데이터로 분리한다.
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print("=" * 30)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# n_estimators : 생성 할 모델의 수
# max_leaf_nodes : 결정트리에 생성할 노드의 최대 갯수
# max_samples: 각 결정 나무를 학습하는 데 사용할 샘플의 개수(int) 
# 혹은 비율(float)
# n_jobs : 사용할 컴퓨터의 코어 갯수를 의미한다. -1을 지정하면 모든 코어를 사용
rnf = RandomForestClassifier(n_estimators = 2, 
                             #트리를 내부적으로 몇 개 만들것인지
                             #성능 테스트를 할때는 각 개수마다 하는게
                             max_leaf_nodes = 16, 
                             max_samples=0.5, 
                             #몇개를 섞을 것인지 0.5 : 50%
                             n_jobs = 1, bootstrap=True)

rnf.fit(X_train,y_train)

#테스트데이터를 이용해서 학습 데이터를 측정한다
y_pred = rnf.predict(X_test)
print(f"정확도 => {accuracy_score(y_pred, y_test)}")
print("=" * 30)

#정답 예측하기
#setosa => 0 / versicolor => 1 / virginica => 2
species = ["setosa" , "versicolor", "virginica"] 

test_data = [ [ 4.3, 2., 6.1, 2.7 ] ]
predict = rnf.predict(test_data)
print(rnf.predict_proba(test_data))
print(predict)
print(species[predict[0]])
print("=" * 30)

