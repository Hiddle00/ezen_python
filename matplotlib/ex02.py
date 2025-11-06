# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:36:35 2025

@author: MYCOM
"""
#선그래프

import matplotlib.pyplot as plt
import numpy as np
plt.rc("font", family="Malgun Gothic")

x = np.arange(1, 6)
y = np.array([10, 15, 7, 12, 15])

plt.plot(x, y, color="blue", linestyle="-", marker="o",
         label="범례",linewidth="2")
#color : 선색, linestyle : 선종류, marker : 마커종류
#linewidth : 선두께
plt.show()

#막대그래프 : x범례, y값
category = ["A", "B", "C", "D"]
value = [4, 1, 7, 8]

plt.bar(category, value,
        #color="orange",
        color=["orange", "blue", "red", "yellow"],
        #지정하지 않아 부족한 색은 반복된다
        edgecolor="black", linewidth=1, width=0.4,
        label="막대그래프")
#edgecolor : 막대 테두리 색
#linewidth : 막대 테두리 두께
#width : 막대 두께
plt.legend()
plt.show()

#수평(horigental) 막대그래프
plt.barh(category, value)
plt.show()


#히스토그램
#도수분포표를 그래프로 나타낸것

#정규분포
#평균을 중심으로 좌우대칭인 종 모양의 확률분포

#넘파이 정규분포 랜덤숫자 1000개 생성
data = np.random.randn(1000)
#randn : 표준 정규분포의 난수 / 범위지정 불가
#표준편차가 1인 가우시안 정규분포를 따른다

#rand : 0 ~ 1 사이의 균일 분포의 난수
print(data)

plt.hist(data, bins=500, color="purple", alpha=0.7)
#bins : 구간의 개수
#alpha : 투명도 0에 가까울수록 투명
plt.show()


#산점도
x = np.random.rand(50) # 0 ~ 1 사이의 난수 50개 균일하게
y = np.random.rand(50)
# s = (점의 크기)
plt.scatter(x, y, s=30, c="red",
            alpha=0.7, edgecolor="black", linewidth=1)
# s : 점의 크기
# c : 점의 색
plt.show()

x_1 = np.random.rand(50) * 0.5
y_1 = np.random.rand(50) * 0.5

x_2 = np.random.rand(50) * 0.5 + 0.5
y_2 = np.random.rand(50) * 0.5 + 0.5
#0.5 ~ 1 사이의 실수 50개

plt.scatter(x_1, y_1, c="blue")
plt.scatter(x_2, y_2, c="red")
plt.show()


#파이차트
label = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]
colors = ["gold", "blue", "red", "green"]
plt.pie(sizes, labels=label, autopct="%1.1f%%", colors=colors,
        startangle=90)
plt.show()
#autopct="%1.1f%%"
#비율표시
#1.1f : 소숫점첫째자리, 1.2f : 소숫점둘째자리
#%% : %문자열

plt.pie(sizes, labels=label, autopct="%1.0f%%", colors=colors,
        explode=(0, 0.1, 0, 0))
#explode : 특정 조각 강조, 두번째 조각
#조각 : label("A")
plt.show()



