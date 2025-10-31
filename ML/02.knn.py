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
df = pd.read_csv("gender.csv")
print(df.head())
print("=" * 30)