# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 09:50:18 2025

@author: MYCOM
"""
#pymysql로 insert쿼리
import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    database="pytest",
    charset="utf8mb4"
)

cursor = conn.cursor()

#insert into users(name,age,email)
#valuse('홍길동', 20, 'hong@test.com')
query = """
insert into users(name, age, email)
values(%s, %s, %s);
"""

cursor.execute(query, ('홍길동', 20, 'hong@test.com'))
conn.commit() #insert 쿼리로 변경된 사항 영구 저장

"""
bulk insert
insert into users(name,age,email)
valuse
('홍길동', 20, 'hong@test.com'),
('전우치', 30, 'hong@test.com'),
('이몽룡', 40, 'lee@test.com'),
"""
#벌크 인서트
#python에선 리스트로 insert하면 된다
data = [
    ("전우치", 30, "jeon@a.com"),
    ("성춘향", 27, "sung@a.com"),
    ("김철수", 31, "kim@a.com")
]
cursor.executemany(query, data)
conn.commit()

cursor.close()
conn.close()
print("연결 종료")