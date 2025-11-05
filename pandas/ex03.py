# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 09:42:23 2025

@author: MYCOM
"""

#데이터프레임에서 데이터 선택
import pandas as pd

data = [
        [15, "남", "전주중"],
        [16, "여", "전주중"],
        [17, "남", "전주고"],
]
idx = ["홍길동", "성춘향", "전우치"]
cols = ["나이", "성별", "학교"]

df = pd.DataFrame(data, columns = cols, index= idx)
print("--" * 20)

#1. 특정 열(컬럼) 선택
print(df["나이"])
#컬럼을 하나만 선택하면 값이 시리즈로 반환
#print(df["이름"]) 오류
#존재하지 않는 컬럼을 가져오려고 하면 에러
print("--" * 20)

print(df[["나이", "성별"]])
#여러개의 컬럼을 선택 할 때 [[]]2차원 배열로 입력해야 한다
print("--" * 20)

#2. 특정 열을 선택해 새로운 데이터프레임 생성
series = df["나이"]
print(series)
print("--" * 20)

#3. 특정 행 선택  /  2가지 함수로 가능
print(df.iloc[0]) #  iloc = integer location
#정수 인덱스 기반 선택(0, 1, 2, 3, ...)
print("--" * 20)

print(df.loc["전우치"])
#라벨 인덱스 기반 선택("홍길동", "성춘향, "전우치)
print("--" * 20)


#4. 특정 값 선택
print(df.iloc[0, 0])
print(df.loc["성춘향", "학교"])
print(df.iloc[0]["나이"])
#print(df.iloc[0]["0"])
