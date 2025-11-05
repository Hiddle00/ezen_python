# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 12:07:55 2025

@author: MYCOM
"""
#판다스의 유틸함수
import pandas as pd

#1. 데이터 전처리
df = pd.read_csv("people.csv", encoding="euc-kr")
print(df)
df = df.drop(columns="세대수")
print(df)
print("--" * 20)
print(df.columns[4:])
df = df.drop(columns=df.columns[4:])
#4번 열  ~ 끝 열 까지 삭제
print(df)
print("--" * 20)
df.columns = ["동", "합계", "남", "여"]
#컬럼 이름 변경
print(df)
print("--" * 20)



df.to_csv("people_proc.csv", index=False)

print(df.columns)
df.to_excel("jeonju_people.xlsx")

print("--" * 20)
#2. 유틸함수(통계)

#2-1. 평균
print(df["합계"].mean())
#전주 총 인구수 동별 평균

print(df["여"].mean())
#전주 여자 인구수 동별 평균


#2-2. 합계
print(df["합계"].sum())
m = df["남"].sum()
fm = df["여"].sum()
print(m + fm)

#2-3. 최대
print(df["합계"].max())

#2-4. 중간
print(df["합계"].median())

#2-5. 최소
print(df["합계"].min())

#3. 집계의 라벨찾기
#최대, 중간, 최소값을 가지고있는 행 번호를 찾는다.
print(df["합계"].idxmax())
print(df.iloc[30])

idxmin = df["합계"].idxmin()
print(df.iloc[idxmin])

print(df.iloc[0])
