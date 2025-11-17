# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:42:53 2025

@author: MYCOM
"""
#get요청 파라미터, post요청 파라미터 처리
from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
#세션 암호화 키 설정
app.secret_key = "b"   #세션 탈취를 막기위한 기본키
#get파라미터 처리
@app.route("/search")
def search() :
    print(request.args)
    print(request.args.get("a"))
    keyword = request.args.get('a')
    # /search?a=...
    #if keyword != None :   == or is
    if keyword :
    #keyword가 false인 상황
    #None, "", 0, False면 False취급
        return f"검색어 : {keyword}"
    return "검색"


#post파라미터 처리
#login 화면 렌더링
@app.route("/login", methods=["GET"])
def login() :
    return render_template("login.html")
    #templates/login.html
#login 처리
@app.route("/login", methods=["POST"])
def loginok() :
    print(request.form)
    id = request.form.get("username")
    pw = request.form.get("password")
    print(id, pw)
    #PRG
    #Post Redirect Get
    #포스트 처리 끝나면 반드시 리다이렉트
    #화면을 요청할
    
    #session객체의 id키에 id값 저장
    #session = {
    # "id" : id
    # }
    session["id"] = id
    return redirect("/search")

@app.route("/")
def home() :
    if "id" in session :
        return f"환영합니다 {session['id']}님"
    else :
        return "로그인 해주세요"
    #세션이 있으면 "환영합니다 ~~님"
    #세션이 없으면 "로그인 해주세요"

@app.route("/logout")
def logout() :
    #del session~~ 도 가능은 하다
    session.pop("id", None) #조금 더 안전한 처리
    return redirect("/login")

app.run(debug=True)
