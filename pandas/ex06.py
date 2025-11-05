# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 11:24:22 2025

@author: MYCOM

import os
print(os.getcwd())
"""

#파이썬의 작업경로 변경
import os
#현재 작업경로
print(os.getcwd())
#현재 작업경로 변경
#os.chdir("D:\YH\ezen_python\pandas")




#데이터 파일 읽기 및 저장
#csv : comma seperated value

#1. csv파일 읽기

import pandas as pd
df = pd.read_csv("data.csv")
#csv파일을 읽을 때 기본 인코딩은 utf-8
#utf-8형식이 아닌 파일을 읽으려면 직접 인코딩 지정
print(df)
print("--" * 20)
print(df.loc[0]["이름"])
print("--" * 20)
print(df.drop(index=0))

#2. csv파일 저장
df.to_csv("output.csv")

#2-2. csv 파일 저장 옵션
df.to_csv("oytput2.csv", index=False)
#인덱스 저장X

df.to_csv("oytput3.csv", index=False, encoding="euc-kr")
#인덱스 저장X, 인코딩방식은 euc-kr
#ansi로 된 파일은 read()할때 파라미터로 지정해줘야 한다.
