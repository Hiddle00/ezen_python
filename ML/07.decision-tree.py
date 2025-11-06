# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 14:02:12 2025

@author: MYCOM
"""
#의사결정 트리 알고리즘
import warnings
warnings.filterwarnings("ignore")
import pandas as pd


iris_df = pd.read_csv("iris_encode.csv")
print(iris_df.head())
print("--" * 25)

#각 컬럼과 데이터 간의 관계확인을 위한 시각화
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc("font", family="Malgun Gothic")

plt.figure(figsize=(12,12))
plt.subplot(2, 2, 1)
#row, columns, index
sns.boxplot(data=iris_df, x="sepal_length", 
            y="species", orient="h");
plt.title("꽃받침 길이")

plt.subplot(2, 2, 2)
sns.boxplot(data=iris_df, x="sepal_width", y="species", orient="h");
plt.title("꽃받침 너비")

plt.subplot(2, 2, 3)
sns.boxplot(data=iris_df, x="petal_length", y="species", orient="h");
plt.title("꽃잎 길이")

plt.subplot(2, 2, 4)
sns.boxplot(data=iris_df, x="petal_width", y="species", orient="h");
plt.title("꽃잎 너비")

#컬럼별 상관관계 시각화
sns.pairplot(data=iris_df, hue="species");
#같은 데이터를 비교하면 산점도가 나오지 않고 선그래프가 나오는 이유
#pair : 짝지은 데이터끼리 연관성을 보는 그래프

#Decision Tree를 이용한 학습과 분류
from sklearn.tree import DecisionTreeClassifier

iris_tree = DecisionTreeClassifier()

#독립변수 : petal_length, petal_width
#종속변수 : species

X = iris_df[["petal_length", "petal_width"]]
print(X)
y = iris_df["species"]
print(y)
print("--" * 25)
#Decision Tree로 학습
iris_tree.fit(X,y)

# 학습결과에 대한 정확도 확인
from sklearn.metrics import accuracy_score
y_pred = iris_tree.predict(X)
score = accuracy_score(y, y_pred)
print(score)

#DecionsTree 시각화
from sklearn.tree import plot_tree

plt.figure(figsize=(10,10))
plot_tree(iris_tree, filled=True)
plt.show()

#==========================================================
#과적합(Overfitting) 검출을 위한 결정경계
#과적합이란 : 학습데이터에 과도하게 적합하게 되어 다른 
#데이터의 정답률(예측)이 감소하는 것

#결과 분석 : 1,2번 사이의 경계선이 복잡하고, 위에서 정확도를 
#구했을 때, 99%가 나왔는데 이것은 과적합된 것이다.
from mlxtend.plotting import plot_decision_regions
import matplotlib
import numpy as np

matplotlib.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(14,8))
feature = np.array(X)
target = np.array(y)
plot_decision_regions(X=feature, y=target, clf=iris_tree, legend=2)
plt.title("결정 경계")
plt.show()

#정답 예측하기
test_data = [[4.3, 2.], [1.2, 1.]]
predict = iris_tree.predict(test_data)
print(predict)




#같은 데이터를 비교하면 산점도가 나오지 않고 선그래프가 나오는 이유
#orient="h",티커
