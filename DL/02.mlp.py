# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 15:23:23 2025

@author: MYCOM
"""
#인공신경망 다층(은닉층) 신경망 퍼셉트론 알고리즘(MLP)
#Multi Layer Perceptron
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
#데이터들의 평균과 분산값을 구한다
print(X_train[0:5])
print("--" * 25)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)
#구한 평균과 분산을 바탕으로 데이터를 스케일링한다.
print(X_train[0:5])
print("--" * 25)



#MLP 모델을 생성한다
from sklearn.neural_network import MLPClassifier
#함수의 기본세팅은 Lelu

# MLP 알고리즘 로드 및 Hidden Layer를 할당
# 함수의 파라미터로 hidden_layer_sizes=(10,10,10)과 
# 같이 설정했는데, 
# 이것은 3개의 은닉층을 만들고 각 계층별로 10개의 노드씩 
# 할당하라는 명령어이다.
mlp = MLPClassifier(hidden_layer_sizes=(10,10,10,10,10))

mlp.fit(X_train,y_train)


#테스트 데이터를 이용해 학습률을 확인
y_pred = mlp.predict(X_test)
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

test_data = [ [ 5.1, 3.4, 1.5, 0.4 ] ]
test_data = sc.transform(test_data)
print(test_data)
predict = mlp.predict(test_data)
print(predict)
print(species[predict[0]])
print("=" * 30)