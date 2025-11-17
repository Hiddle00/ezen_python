# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:20:42 2025

@author: MYCOM
"""
#flask는 파이썬 기반의 가벼운 웹 프레임워크
#파이썬 웹 프레임워크 3대장
#1. django 
#2. flask 규모가 커지면 무거워진다
#3. fastapi
#문법은 1,2가 거의 같고 3만 조금 다르다

#pip install flask
from flask import Flask

#flask 웹 어플리케이션 객체 생성
app = Flask(__name__) #생성자호출
#__main__

#경로(라우트)
@app.route("/") #flask의 함수에선 항상 return필요
def home() :
    return "home! alaskfji"

@app.route("/a")
def a() :
    return "A!"

#동적 라우트(path variable)
@app.route("/user/<name>")
def user(name) :
    return f"안녕하세요 {name}님"

#url설계 원칙
#1. 대문자 X : /User/<name>
#2. 언더바(_) X : /user_find/  -> 대시(-)사용 : /user-hong
#3. 경로로 자원의 위치를 표시
# board/1    O
# board?no=1 X
#4. url은 동사 X : /find-user
#5. url에 행위(db동작) 묘사 X 
# /user         O
# /user/select  X

#flask 웹 어플리케이션 실행
#flask의 기본 포트 : 5000
app.run(debug=True) 
#app.run(debug=True) 수정한 코드가 실시간으로 반영됨