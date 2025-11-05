# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 09:11:03 2025

@author: MYCOM
"""

import pandas as pd
#데이터프레임
#판다스의 2차원 자료구조
#여러개의 시리즈가 함쳐진 집합

#시리즈의 값은 1차원 넘파이로 반환
a = {
     "b" : "c"
}

a.get("b")    #방식이 다르다 없으면 None
a["b"]        #없으면 에러 발생


a = {
     "b" : [1, 2, 3]
}
a["b"][0]
"""--------------------------------------------"""

data = {
    "이름" : ["길동", "철수", "춘향"],
    "나이" : [25, 30, 25],
    "거주지" : ["인천", "순천", "동해"]
}

df = pd.DataFrame(data)
print(df)

#데이터프레임의 속성(인덱스,값,)
print(df.index)     #데이터프레임의 행 인덱스
print("--" * 20)

print(df.columns)   #데이터프레임의 컬럼(열 이름)
print("--" * 20)

print(df.values)    #데이터프레임이 가지고 있는 값(2차원 넘파이 배열)
print("--" * 20)

print(df.dtypes)    #각 열의 데이터 타입들
print("--" * 20)

print(df.shape)     #(행, 열) 크기
print("--" * 20)


#리스트를 이용한 데이터 프레임 생성
data = [
    [15, "남", "전라중"],
    [16, "여", "전라중"],
    [17, "남", "전라고"]
]           # 리스트를 사용하면 그대로 변환됨(세워지지 않음)

df = pd.DataFrame(data)
print(df)
print("--" * 20)

#인덱스, 컬럼, 데이터를 나누어서 데이터프레임 생성
idx = ["홍길동", "성춘향", "전우치"]
cols = ["나이", "성별", "학교"]

df = pd.DataFrame(data, index = idx, columns = cols)
print(df)