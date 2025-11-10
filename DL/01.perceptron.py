# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 14:37:42 2025

@author: MYCOM
"""
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.model_selection import train_test_split

iris_df = pd.read_csv("iris_encode.csv")
# 독립 변수(X : sepal_length, sepal_width, petal_length, petal_width)
X = iris_df[ ["sepal_length", "sepal_width", "petal_length", "petal_width"] ]
print(X)
print("--" * 25)
# 종속 변수(y : species)
y = iris_df["species"]
print(y)
print("--" * 25)

# 독립변수(X)와 종속 변수(y)를 각각 훈련 데이터와 테스트 데이터로 분리한다.
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
print("--" * 25)

# 데이터를 스케일링 한다. (StandardScale)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X)
print(X_train[0:5])
print("--" * 25)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
print(X_train[0:5])
print("--" * 25)

# 퍼셉트론을 이용하여 학습을 수행한다.
from sklearn.linear_model import Perceptron

# eta0 = 학습률, max_iter = epoch
# random_state = 1, 에포크마다 훈련 세트를 
# 섞은 결과가 나중에 재현되도록
pr = Perceptron(random_state = 2, max_iter = 1000, 
                eta0 = 0.5 )
pr.fit(X_train, y_train)

#테스트 데이터를 이용해 학습률을 확인
y_pred = pr.predict(X_test)
print(list(y_test))
print("--" * 25)
print(list(y_pred))
print("--" * 25)
err= (y_test != y_pred)
print("잘못 분류된 갯수 : %d" % err.sum())
print("정확도 : %f" % (100 - (err.sum()/len(y_test))))


#정답 예측하기
#setosa => 0 / versicolor => 1 / virginica => 2
species = ["setosa" , "versicolor", "virginica"] 

test_data = [ [ 4.3, 2., 6.1, 2.7 ] ]
predict = pr.predict(test_data)
print(predict)
print(species[predict[0]])
print("=" * 30)