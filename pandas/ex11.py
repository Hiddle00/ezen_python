# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 10:33:23 2025

@author: MYCOM
"""
#결측값 찾기,처리
import pandas as pd

df = pd.read_csv("people_broke2.csv")
print(df)
print("--" * 25)

"""
print(df.info())
#df의 간단한 정보 출력
print("--" * 25)

print(df.head())
#상위 5개의 데이터만 출력
print("--" * 25)

print(df.tail())
#하위 5개의 데이터
print("--" * 25)

print(df.head(7))
#상위 7개의 데이터만 출력
print("--" * 25)
"""

#결측값 확인
#결측값 : 데이터에서 누락된 값(NaN : Not a Number)

print(df.isnull())
#각 열의 결측값 확인
#결측값이 있는 곳에 True로 표기

print(df.isnull().sum())
#각 열에 있는 결측값을 합산해 표기
#각 열별로 결측값의 갯수를 확인

print(df["남"].isnull().sum())
#남 열의 결측값 갯수를 확인

print(df.notnull().sum())
#각 열별로 결측값이 아닌 갯수를 확인


#2. 결측값 조건 검색
print(df[df.isnull().any(axis=1)])
#한 행에 결측값이 하나라도 존재하는 데이터를 조회

print(df.drop(columns = "동"))
#"동" 컬럼 삭제 후 데이터 조회

print(df.isnull().all(axis=1))
#한 행의 모든 컬럼이 결측값인 행 조회
#없음 : "동"컬럼이 결측값인 행이 없음

print(df.drop(columns = "동").isnull().all(axis=1))
#"동"컬럼만 제외하고 모든 컬럼이 결측값인 모든 행 조회
print(df[df.drop(columns = "동").isnull().all(axis=1)])
print(df[df.drop(columns = "동").isnull().all(axis=1)].drop(columns = "동"))

#3. 결측값 대체
print(df.fillna(0))
#모든 결측값을 0으로 대체

print(df["남"].fillna(0))
#"남"컬럼의 결측값을 0으로 대체

print(df["합계"].fillna(df["합계"].mean()))
#--------->
print(df[df["합계"] != df["남"] + df["여"]])
print(df[df.isnull().any(axis=1)])

#4.결측값 제거
print(df.dropna(axis=0))
#모든 행에 대해 결측값이 포함된 행을 제거

print(df.dropna(axis=1))
#모든 행에 대해 결측값이 포함된 열을 제거

#df.dropna(axis=0, inplace=True)

print(df.dropna(subset=["여"], axis=0))
#"여"컬럼에 결측값이 포함되어있는 행을 삭제


#5.중복행 제거
print(df.drop_duplicates())
#모든 데이터에서 동일한 값이 들어있는 중복된 행 삭제
print(df.drop_duplicates(subset=["동"]))
#"동"컬럼에 중복된 값이 있다면 해당 행 삭제
#아래에서부터 삭제한다
print(df["동"].drop_duplicates())
