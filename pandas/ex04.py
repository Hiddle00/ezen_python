# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 10:03:05 2025

@author: MYCOM
"""
#데이터프레임 조작
import pandas as pd

data = [
        [15, "남", "전주중"],
        [16, "여", "전주중"],
        [17, "남", "전주고"],
]
idx = ["홍길동", "성춘향", "전우치"]
cols = ["나이", "성별", "학교"]

df = pd.DataFrame(data, columns = cols, index= idx)

#1. 컬럼 이름 변경
print(df.columns)
df.columns = ["age", "gender", "school"]
print("--" * 20)
print(df.columns)
print(df)
print("--" * 20)

#2. 인덱스 이름 변경
df.index = ["hong", "sung", "jeon"]
print(df.index)
print(df)
print("--" * 20)


#3. 데이터 변경
df.loc["jeon", "age"] = 14      # "jeon"행의 "age"컬럼 값을 14로 변경
df.loc["jeon", "나이"] = 14     # "jeon"행의 "나이"컬럼이 없다면 생성하고 값을 14로 지정
print(df)
print("--" * 20)

df["school"] = "전주중"         # "school"컬럼의 모든 값을 "전주중"으로 변경
print(df)
print("--" * 20)

# 불리안 인덱스(Boolean index)
print(df["age"] > 15)
print("--" * 20)
print(df[[ False, True, False]])
print(df[df["age"] > 15])
print("--" * 20)

df.loc[df["age"] > 15 , "school"] = "전주고"
#df.loc[df["age"] > 15 , "gender"] = "female"
#age가 16보다 큰 행의 school컬럼의 값을 "전주고"로 변경
print(df)
print("--" * 20)



