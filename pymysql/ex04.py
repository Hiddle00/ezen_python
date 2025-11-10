# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:10:43 2025

@author: MYCOM
"""
#pymysql로 select쿼리 실행
import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    database="pytest",
    charset="utf8mb4"
)

cursor = conn.cursor()

#select * from users;
cursor.execute("select * from users")
row = cursor.fetchone()
#실행 후 결과물을 가져온다
#쿼리의 실행 결과에서 첫번째 행만 조회
#조회 결과가 튜플로 반환
#fetchall(), fetchmany
print(row)

#구조분해 할당으로 조회한 결과를 변수에 분리
id, name, age, email, create_date = row

print(id, name, age, email, create_date)

#여러개 select
cursor.execute("select * from users")
rows = cursor.fetchall()
print(rows)

#(
#  (id, name, age, email, create_date),
#  (id, name, age, email, create_date),
#)

for row in rows :
    print(row)


cursor.close()
conn.close()
print("연결 종료")
