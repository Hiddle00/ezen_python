# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 10:29:19 2025

@author: MYCOM
"""
#pymysql의 update
import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    database="pytest",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
    #조회 결과를 딕셔너리로 매핑
)

cursor = conn.cursor()

#update users set name = ?, age = ?, email = ?
query = """
update users set
    name = %s,
    age = %s,
    email = %s
where id = %s
"""

cursor.execute(query, ('홍길동', 25, 'h@a.com', 1))
conn.commit()

cursor.execute("select * from users where id = 1")
row = cursor.fetchone()
print(row)


#데이터 삭제
#delete from users where id = ?
query = """
delete from users where id = %s
"""

cursor.execute(query, (1,))
conn.commit()

try :
    query = """
    insert into users(name, age, email)
    values('짱구', 5, 'jj@a.com')
    """
    #쿼리 실행
    cursor.execute(query)
    #정상실행 되면 commit
    conn.commit()
except :
    #문제가 발생했으면 rollback(취소)
    conn.rollback()
    print("예외처리")
finally :
    #반드시 자원 회수
    cursor.close()
    conn.close()
    
cursor.close()
conn.close()
print("연결 종료")