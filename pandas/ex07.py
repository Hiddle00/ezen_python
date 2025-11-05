# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 11:53:38 2025

@author: MYCOM
"""

#엑셀파일 읽기 & 저장

import pandas as pd

#1. excel 파일 읽기
df = pd.read_excel('data.xlsx', sheet_name="Sheet1")
print(df)
#not found에러가 발생하면 
#1. pip install openpyxl
#2. Sheet 이름 명시 

#2. excel 파일 저장
df.to_excel("output.xlsx")
df.to_excel("output2.xlsx", index=False)

#3. csv 파일로 저장
df.to_csv("output4.csv", index=False)

#4. json 파일로 저장
df.to_json("output.json", force_ascii=False, orient="records", indent=4)
#귀찮은 작업이 많다
#force_ascii : 아스키 형태로 저장X
#orient : 각 행을 json 객체로 변환
#indent : 들여쓰기(4칸)