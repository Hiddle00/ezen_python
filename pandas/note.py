# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 09:09:48 2025

@author: MYCOM
"""

import matplotlib.pyplot as plt
import numpy as np
plt.rc("font", family="Malgun Gothic")

x = np.arange(1, 6)
y = np.array([10, 15, 7, 12, 15])

plt.plot(x, y, color="blue", linestyle="-", marker="o",
         label="범례",linewidth="2")

category = ["A", "B", "C", "D"]
value = [4, 1, 7, 8]

plt.bar(category, value)

import pandas as pd
import matplotlib.pyplot as plt

#1. 데이터(csv파일)로드
df = pd.read_csv("AB_NYC_2019.csv")
#2019년 뉴욕에 영업중인 AirBnB 업장
#강제로 모든 행을 출력하려면 반복문으로 해야한다
#print(df)

#데이터의 기본 탐색
print(f"데이터의 크기 : {df.shape}")
#48,895행, 16열

print(f"컬럼 목록 : {df.columns}")

"""
아이디, ~ , 지역구, ~ , 위경도
'id', 'name', 'host_id', 'host_name', 'neighbourhood_group'주,
       'neighbourhood'세부구역, 'latitude'위도, 'longitude', 'room_type', 'price' 1박/$,
       'minimum_nights', 'number_of_reviews', 'last_review',
       'reviews_per_month', 'calculated_host_listings_count',
       'availability_365'
"""
print("--" * 25)

#데이터 샘플(상위 5개 행)
print(df.head())
print(df[["name", "price"]])
print("--" * 25)
print(df.info())
print(df.duplicated().sum())

print(df.groupby("neighbourhood_group")["price"].mean())


import folium
from folium.plugins import HeatMap

nyc_map = folium.Map(location=[40.7128, -74.0060], zoom_start=11)
heat_data = list(zip(df['latitude'], df['longitude'], df['price'])) 
HeatMap(heat_data, radius=10).add_to(nyc_map)
nyc_map.save("nyc_heatmap.html")
