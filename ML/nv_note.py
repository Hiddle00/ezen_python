# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 09:19:03 2025

@author: MYCOM
"""
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
from konlpy.tag import Okt

df = pd.read_excel("nv_data.xlsx")
print(df)
print("--" * 25)

okt = Okt()

msg = "나는 오늘 학교에 가서 공부를 열심히 했다."
item = okt.phrases(msg)
print(item)
item = okt.pos(msg)
print(item)
item = okt.morphs(msg)
print(item)

#pos = ['{}/{}'.format()]

import numpy as np
import matplotlib.pyplot as plt

# 예시 데이터
y = np.array([2, 4, 5, 7, 9])  # 관측값
theta = np.linspace(0, 10, 200)  # θ 범위
S_theta = np.sum((y[:, None] - theta[None, :])**2, axis=0)  # S(θ) 계산

# 최소점
theta_hat = np.mean(y)
S_min = np.min(S_theta)

# 그래프 그리기
plt.figure(figsize=(8,5))
plt.plot(theta, S_theta, label=r'$S(\theta)=\sum(y_i-\theta)^2$')
plt.scatter(theta_hat, S_min, color='red', zorder=5, label=f'Min at θ={theta_hat:.2f}')
plt.title(r'Graph of $S(\theta)$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$S(\theta)$')
plt.legend()
plt.grid(True)
plt.show()



# 데이터 생성
X = np.array([1, 2, 3])
Y = np.array([4, 5, 6])

# 평균 계산
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# 편차 계산
dev_X = X - mean_X
dev_Y = Y - mean_Y

# 편차의 제곱
dev_X_sq = dev_X ** 2
dev_Y_sq = dev_Y ** 2

# 분산 계산
var_X = np.mean(dev_X_sq)
var_Y = np.mean(dev_Y_sq)

# 공분산 계산
cov_XY = np.mean(dev_X * dev_Y)

# 그래프 시각화
fig, ax = plt.subplots(figsize=(8, 6))

# X, Y 데이터 플롯
ax.plot(X, Y, 'bo', label="Data points (X, Y)")

# X와 Y의 평균선 (수평선, 수직선)
ax.axvline(mean_X, color='r', linestyle='--', label="Mean of X")
ax.axhline(mean_Y, color='g', linestyle='--', label="Mean of Y")

# X와 Y의 편차 제곱
ax.plot(X, dev_X_sq, 'ro', label="Squared Deviations of X")
ax.plot(Y, dev_Y_sq, 'go', label="Squared Deviations of Y")

# 텍스트로 분산과 공분산 값 표시
ax.text(2.5, 5.5, f"Var(X) = {var_X:.3f}", fontsize=12, color='red')
ax.text(2.5, 4.5, f"Var(Y) = {var_Y:.3f}", fontsize=12, color='green')
ax.text(2.5, 3.5, f"Cov(X, Y) = {cov_XY:.3f}", fontsize=12, color='blue')

# 레이블, 제목, 범례
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Variance and Covariance Visualized')
ax.legend()

plt.grid(True)
plt.show()