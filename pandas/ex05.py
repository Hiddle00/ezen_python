# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 10:23:31 2025

@author: MYCOM
"""

# 데이터 추가 & 삭제
import pandas as pd

data = [
        ["홍길동", 17, "전주"],
        ["성춘향", 16, "전주"],
        ["전우치", 15, "익산"],
]

cols = ["이름", "나이", "거주지"]
df = pd.DataFrame(data, columns = cols)
print(df)

#1. 컬럼(새로운 열) 추가
df["점수"] = [70, 80, 60]
print(df)
print("--" * 20)


#2. 새로운 행 추가
new_data = [
    ["철수", 19, "런던"]
]
new_df = pd.DataFrame(new_data, columns= cols)
new_df["점수"] = 91
print(new_df)

df = pd.concat([df, new_df], ignore_index= True) #뒤에 붙이는 df의 인덱스를 무시할건지
#df와 new_df를 결합
#df아래에 new_df가 행으로 추가, new_df의 index 무시
print(df)
print("--" * 20)


#3. 행 삭제
#영구 반영하려면 두 가지 선택지 중 선택해야 한다
#원본에는 영향없이 복사한 새로운 행에서만 영향이 가기 때문에 원본에 반영을 따로 해주어야 한다
df.drop(index = 0, inplace=True)
#df = df.drop(index = 0)
print(df)
print("--" * 20)
#drop함수는 원본 df를 복제 후 복제된 df에서만 삭제한다.
#결과가 반영된 복제 df를 반환 => drop해도 원본에는 영향 X
#inplace속성은 결측값과 관련해서 동작은 하지만 반영이 안될때가 있다.


#4. 열 삭제
df = df.drop(columns="점수")
print(df)
#drop함수의 inplace가 True면 대입없이 원본에 삭제된 결과가 반영된다. 기본값은 False
print("--" * 20)


#정렬
df = df.sort_values(by="나이", ascending=False)
#나이컬럼 기준으로 내림차순 정렬 (ascending(오름차순)이 거짓)
#정렬해도 데이터프레임 원본에는 반영 X
print(df)
print("--" * 20)

df = df.sort_values(by="이름")
#이름컬럼 기준으로 오름차순 정렬(기본값)
print(df)
print("--" * 20)

df = df.sort_values(by=["나이", "이름"], ascending=[True, False])
#나이컬럼 기준으로 오름차순 정렬 후, 나이가 같으면 이름기준으로 내림정렬
print(df)
print("--" * 20)


