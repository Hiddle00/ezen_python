# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 12:02:19 2025

@author: MYCOM
"""
#matplotlib의 figure와 axes
#figure : 전체 그래프가 그려지는 영역(캔버스)
#axes : figure 내에서 개별적인 그래프가 그려지는 부분

import matplotlib.pyplot as plt
figure, ax = plt.subplots()

ax.plot([1,2,3,4], [1,2,3,4])
ax.set_xlabel("x축")
#직접적으로 함수를 사용하지 못하고 세터 매서드를 사용한다?
ax.set_ylabel("y축")
ax.set_title("피규어")
plt.show()

figure, ax = plt.subplots(1, 2, figsize=(10,4))
#1행 2열의 axes를 생성
#figure는 하나
#axes를 생성할 때 가로10 세로 4 크기

ax[0].plot([1,2,3,4], [1,2,3,4])
ax[1].bar([1,2,3,4], [1,2,3,4])
#plt.xlabel() -> ax.set_xlabel()
#plt.title() -> ax.set_title()

plt.show()

fig, ax = plt.subplots(2, 1, figsize=(6, 10), sharex=True)
#티커
ax[0].scatter([1,2,3,4], [1,2,3,4])
ax[1].plot([1,2,3,4], [1,2,3,4])
plt.show()

fig, ax = plt.subplots(2, 2, figsize=(10,8))
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
#ax[0][0]
ax[0, 0].plot(x, y, color="blue")
ax[0, 0].bar(x, y, color="red")
ax[0, 0].scatter(x, y, color="green")
ax[0, 0].hist(x, color="yellow")
ax[0, 1].bar(x, y, color="red")
ax[1, 0].scatter(x, y, color="green")
ax[1, 1].hist(x, color="yellow")
plt.show()
