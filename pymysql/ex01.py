# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 09:18:42 2025

@author: MYCOM
"""
#pymysql
#python에서 mysql을 연결하고 쿼리를 실행하는 라이브러리
#pip install pymysql

import pymysql

#mysql db서버와 연결
#mysql -u root -p -H localhost -P 3306
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    database="test",
    charset="utf8mb4"
)

print(conn)

#쿼리 실행 객체
#연결정보로 쿼리 실행 객체를 만들어야한다
cursor = conn.cursor()

#쿼리 실행
#정상적인 쿼리면 실행됨
cursor.execute("쿼리...")

#쿼리 실행 객체 자원 회수
cursor.close()
#연결 객체 자원 회수
conn.close()

#create database pytest;