# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 10:01:06 2025

@author: MYCOM
"""

import pandas as pd


data = {
    "나이" : [20, 30, 40, "50세"],
    "이름" : ["철수", "영희", "짱구", "맹구"],
    "지역" : ["전주", "서울", "경기", "청주"]
}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)

def to_int(v):
    if isinstance(v, str) :    
        v = v.replace("세", "")
    return int(v)
    
df["나이"] = df["나이"].apply(to_int)

print(type(df.loc[0,"나이"]))
print(type(df.loc[1,"나이"]))
print(type(df.loc[2,"나이"]))
print(type(df.loc[3,"나이"]))
print("--" * 25)
print(df["나이"].sum())

#1.나이컬럼의 모든 데이터의 타입을 str로 변경
print(type(df.loc[0,"나이"]))
print(type(df.loc[1,"나이"]))
print(type(df.loc[2,"나이"]))
print(type(df.loc[3,"나이"]))

df.loc[0,"나이"] = str(df.loc[0,"나이"])
df.loc[1,"나이"] = str(df.loc[1,"나이"])
df.loc[2,"나이"] = str(df.loc[2,"나이"])
df.loc[3,"나이"] = str(df.loc[3,"나이"])

print(type(df.loc[0,"나이"]))
print(type(df.loc[1,"나이"]))
print(type(df.loc[2,"나이"]))
print(type(df.loc[3,"나이"]))

print(df["나이"].sum())
print(df.dtypes)

#2. 나이컬럼의 모든 데이터의 타입을 int로 변경
for i, v in enumerate(df["나이"]) :
    if not isinstance(v, int) :
        result = v.replace("세", "")
        df.loc[i, "나이"] = int(result)

print(type(df.loc[0,"나이"]))
print(type(df.loc[1,"나이"]))
print(type(df.loc[2,"나이"]))
print(type(df.loc[3,"나이"]))

#apply는 내부적으로 c?를 사용하여 연산속도가 빠르다