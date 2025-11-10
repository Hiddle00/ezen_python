# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:22:47 2025

@author: MYCOM
"""
#pymysql의 조회 결과를 dictionary로 받기
import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    database="pytest",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
    #조회 결과를 딕셔너리로 매핑
    #(1, 'hong', 20, 'hong@a.com', '날짜')
    #{id : 1, name : '홍길동', age : 20, ...}
)

cursor = conn.cursor()

cursor.execute("select * from users")
row = cursor.fetchone()
print(row)
#row.id row["id"]

cursor.close()
conn.close()
print("연결 종료")