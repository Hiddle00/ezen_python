# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 14:05:40 2025

@author: MYCOM
"""

# K-Means 알고리즘 
import warnings
warnings.filterwarnings("ignore")

import mglearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

#k-means 알고리즘 설명용 이미지 출력
mglearn.plots.plot_kmeans_algorithm()
plt.show()

iris_df = pd.read_csv("iris_encode.csv")

# 독립 변수(X : sepal_length, sepal_width, petal_length, petal_width)
X = iris_df[ ["sepal_length", "sepal_width", "petal_length", "petal_width"] ]

#KMeans 라이브러리 선언
from sklearn.cluster import KMeans
# K-평균 군집화 모델 생성 및 학습
# n_clusters : 군집 수 3개로 생성
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

print(kmeans.labels_)
iris_df["cluster"] = kmeans.labels_
print(iris_df)


#각 클러스터의 중심점을 출력한다.
centers = kmeans.cluster_centers_
print(f"군집 중심점 : {centers}")

import seaborn as sns

"""
군집 시각화
"""