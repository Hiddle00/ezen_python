# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 09:17:49 2025

@author: MYCOM
"""
#파라미터로 문자열을 받아서 정수로 변환하여 반환하는 함수 생성
#------>
def to_int(text) :
    #파라미터로 받은 값이 정수인지 확인다고 정수면 replace없이 그대로 반환
    if isinstance(text, int) :
        return text
    #파라미터로 받은 문자열에서 쉼표 제거
    result = text.replace(",", "")
    result = result.replace("-", "")
    result = result.replace("명", "")
    return int(result)
#------>



#csv 자료형식이 일치하지 않을 경우 처리방법
import pandas as pd

df = pd.read_csv("people_broke.csv", thousands=",")
# thousands= :천단위 숫자에 쉼표를 찍는다
print(df)
print("--" * 25)
print(df.dtypes)

print(df["합계"].sum())
#문제점 1. 정수형 데이터가 따옴표로 감싸져있어서 문자열취급

#판다스 데이터에 공통적으로 함수 적용하기       &&      apply
df["합계"] = df["합계"].apply(to_int)
#데이터프레임의 합계컬럼의 모든행에 일괄적으로 to_int함수 적용
#to_int의 반환값을 해당 값에 덮어쓴다

for i in enumerate[1, 6] :
    print(i)
    
for i, v in enumerate(df["합계"]) :
    df.loc[i, "합계"] = to_int(v)
#------>
#------>
print(df["합계"].sum())
print("--" * 25)

df["여"] = df["여"].apply(to_int)
print(df["여"].sum())

df["남"] = df["남"].apply(to_int)
print(df["남"].sum())





a = to_int("50000")
print(a)
b = to_int("50,000명")
print(type(b))
print(b)


    
    