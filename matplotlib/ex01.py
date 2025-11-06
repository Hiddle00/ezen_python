# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 09:13:34 2025

@author: MYCOM
"""
# 판다스는 줄글형태
# 데이터를 보려고 사용하는 라이브러리?
# ->더 세부적으로 시각화하는 matplotlib
#데이터 시각화
#2d그래프를 그리는 라이브러리
#선그래프, 바그래프, 히스토그램, 산점도, 파이차트
#pip install matplotlib

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()

plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
#앞의 리스트 : x축, 뒤의 리스트 : y축
#(1, 1), (2, 2), (3, 3), (4, 4)
plt.show()

#축 범위 지정
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis([0, 6, 0, 20])
# x축의 크기를 0 ~ 6, y축의 크기를 0 ~ 20
plt.show()

#선 스타일 지정
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "rv:")
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "g^--")
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "m<-.")
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "y>-")
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "c*-")
#rgb cmy kw 색상 축약어
#16진수 색상코드(#FFFFFF, #000000)

#. , o v ^ < > s *
#점 픽셀 원 삼각형... 사각형 별

#- -- : -.
#실선, 대시선, 점선, 점-대시선

#산점도와 바그래프등은 선이 없다


#여러개의 그래프 그리기
import numpy as np
t = np.arange(0, 5, 0.2)
print(t)

plt.plot(t, t, "r--")
plt.show()
plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g>")
plt.show()

plt.plot(t, t, "r--")
plt.plot(t, t**2, "bs")
plt.plot(t, t**3, "g>")
plt.show()

#그래프 설명
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.xlabel("x-label", loc = "right")
#가로축 라벨 : right, center, left
plt.ylabel("y-label", loc = "top")
#세로축 라벨 : top, middle, bottom
plt.show()

#범례 - legend
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label="price")
plt.legend()
plt.show()

plt.plot([1, 2, 3, 4], [1, 2, 3, 4], label="price")
#plt.legend(loc=(1.0, 1.0))
#plt.legend(loc=(0.5, 0.5))
#plt.legend(loc=(1.0, 0.5))
#plt.legend(loc=(0.0, 0.0))
plt.legend(loc=("lower right"))
plt.show()

plt.plot(t,t,  "g^--", label="price")
plt.plot(t,t**2, "bs", label="price")
plt.plot(t,t**3, "m>", label="price")
plt.legend()
plt.show()

# 축 조절
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
#plt.axis([0, 5, 0, 20])
#xmin, xmax, ymin, ymax
#plt.xlim([0,5]) # x축 범위 xmin, xmax
#plt.ylim([0,20]) # y축 범위 ymin, ymax
plt.axis("scaled") # 실제 범위 내로 축소(확대)
plt.show()

#그래프 제목
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.title("title.......")
plt.show()

#캔버스(figure)의 격자 설정
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.grid(True)
plt.show()



#한글 깨짐 해결
#윈도우 폰트 변경
plt.rc("font", family="Malgun Gothic")

#맥 폰트 변경
#plt.rc("font", family="AppleGothic")

plt.plot([1, 2, 3, 4], [1, 2, 3, 4], "g<", label="가격")
plt.plot(t, t**2, "bs")
plt.plot(t, t**3, "g>")
plt.xlabel("시간")
plt.ylabel("종가")
plt.title("주가그래프")
plt.legend()
plt.grid(True)
plt.show()

#이미지 저장
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.savefig("figure.png")
plt.show()

