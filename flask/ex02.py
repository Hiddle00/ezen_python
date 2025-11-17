# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:23:48 2025

@author: MYCOM
"""
#templates폴더 > html파일들은 이 안에 들어가야 한다.

#html페이지 반환(렌더링)
from flask import Flask, render_template, jsonify  #소문자: 함수 / 대문자: 클래스

app = Flask(__name__)

#GET POST 요청 처리 (없으면 모두 처리)
@app.route("/", methods=["GET"])
#@app.route("/", methods=["GET", "POST"])
def home() :
    return render_template("index.html")
    #templates/index.html 파일을 찾아 화면에 렌더링

#Restful API 만들기
#요청했을 때 데이터만 응답오는 url
@app.route("/users")
def users() :
    #/users -> [{id : 'hong', pw : '1234'}]
    data = [
        {
            "id" : "hong",
            "pw" : "1234"
        },
        {
            "id" : "jeon",
            "pw" : "4321"
        }
    ]
    return jsonify(data)
app.run(debug=True)