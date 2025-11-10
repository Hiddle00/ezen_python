# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 09:37:29 2025

@author: MYCOM
"""
#pymysql로 create쿼리 실행
import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    database="pytest",
    charset="utf8mb4"
)

cursor = conn.cursor()

query = """
create table if not exists users(
	id int auto_increment primary key,
	name varchar(255) not null,
	age int not null,
	email varchar(255) not null,
	create_date timestamp default now()
);
"""

cursor.execute(query)
print("테이블 생성 완료")

cursor.close()
conn.close()
print("연결 종료")