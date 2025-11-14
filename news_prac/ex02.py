# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:19:13 2025

@author: MYCOM
"""
#pymysql을 이용한 수집데이터 저장
#naver_news_data.csv파일을 db에 저장
import pandas as pd
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen"   
)
#굳이 python으로 db를 만들 필요는 없다
#

#특정 데이터베이스 선택 없이 mysql에 연결
cursor = conn.cursor()

#create database news;
#dml?(insert, update, delete 는 commit이나 rollback이 필요하지만
#ddl은 할 수 없다?)
cursor.execute("create database if not exists news")  # news 데이터베이스 생성

cursor.execute("use news;") # news db선택

table_query = """
create table if not exists naver_news(
    id int primary key auto_increment,
    title varchar(255) not null,
    link varchar(255) not null,
    content text not null,
    create_date datetime default now()
)
"""

cursor.execute(table_query) #news db에 naver_news 테이블 생성

#csv파일 로드
df = pd.read_csv("naver_news_data.csv")
#print(df.info())
print(df["제목"].values.tolist())
#values = [value for value in df["제목"]]

#pymysql의 executemany함수로 벌크인서트 처리를 위해 df의 컬럼의 값을 꺼내서
#파이썬의 리스트로 변환
#tolist() -> numpy 배열을 파이썬list로 변환하는 numpy함수
titles = df["제목"].values.tolist()
links = df["링크"].values.tolist()
contents = df["내용"].values.tolist()
data = list(zip(titles, links, contents))

#insert
insert_query = """
insert into naver_news(title, link, content)
values(%s, %s, %s)
"""

#insert는 파라미터를 여러개 줄 수 있지만
#executemany는 하나만 받을 수 있다. 이터rows?
cursor.executemany(insert_query, data)
conn.commit()

cursor.close()
conn.close()

