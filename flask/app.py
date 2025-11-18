from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
@app.route("/join", methods=["GET"])
def join() :
    return render_template("join.html")

@app.route("/join", methods=["POST"])
def joinok() :
    id = request.form.get("id")
    pw = request.form.get("pw")
    nick = request.form.get("nick")
    print(id,pw,nick)
    #post파라미터 3개(id,pw,nick)
    #id 중복체크, 중복시 join페이지로 redirect

    #pymysql로 user테이블에 insert
    return redirect("/login")

@app.route("/login", methods=["GET"])
def login() :
    pass

@app.route("/login", methods=["POST"])
def loginok() :
    pass

@app.route("/modify", methods=["GET"])
def modify() :
    pass

@app.route("/modify", methods=["POST"])
def modifyok() :
    pass

@app.route("/logout", methods=["POST"])
def logout() :
    pass

@app.route("/leave", methods=["POST"])
def leave() :
    pass

app.run(debug=True)