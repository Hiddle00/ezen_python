from flask import Flask, render_template, request, redirect, session
#분리된 라우터 파일 import
from routes.user import user_bp
from routes.note import note_bp
app = Flask(__name__)
app.secret_key = "ezen" #암호화? 복호키?

#분리된 user 라우터를 flask에 등록
app.register_blueprint(user_bp)
app.register_blueprint(note_bp)

#user가 접근하는 url
"""
1. 회원가입
    -> 화면 / join, GET
    -> 처리 / join, POST, insert쿼리, 파라미터(id, pw, nick), redirect
2. 로그인
    -> 화면 / login, GET
    -> 처리 / login, POST, select쿼리, 파라미터(id, pw), redirect
3. 회원정보수정
    -> 화면 / modify, GET
    -> 처리 / modify, POST, update쿼리, 파라미터(id, pw, nick), redirect
4. 로그아웃
    -> 처리 / logout, POST
5. 회원탈퇴
    -> 처리 / leave, POST, delete쿼리
"""
#홈 라우터
@app.route("/", methods=["GET"])
def home() :
    return render_template("home.html")

app.run(debug=True)