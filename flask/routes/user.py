from flask import Blueprint, render_template, request, redirect, session
#import user_dao
#user_dao.UserDAO()
from user_dao import UserDAO

#user에 관련된 라우터 함수들 분리
#@app.route("/login") -> @app.route("/user/login")

# @user_bp 데코레이터가 붙은 라우터는 전부 앞에 /user가 붙는다.
user_bp = Blueprint("user", __name__, url_prefix="/user")


#회원가입 화면 라우터
@user_bp.route("/join", methods=["GET"])
def join() :
    return render_template("user/join.html")

#회원가입 처리 라우터
@user_bp.route("/join", methods=["POST"])
def joinok() :
    id = request.form.get("id")
    pw = request.form.get("pw")
    nick = request.form.get("nick")
    #html의 name 참조
    print(id,pw,nick)
    #post파라미터 3개(id,pw,nick)

    dao = UserDAO()
    count = dao.id_check(id)
    #count == 0 회원가입 가능
    #count == 1 회원가입 불가능
    #id 중복체크, 중복시 join페이지로 redirect
    if (count == 0) :
        #pymysql로 user테이블에 insert
        dao.join(id,pw,nick)
        return redirect("/user/login")
    return redirect("/user/join")

#vo사용시 vo import
#user = UserDAO(id,pw,nick)
#execute 할때 user.id, user.pw

#로그인 화면 라우터
@user_bp.route("/login", methods=["GET"])
def login() :
    if session.get("user") :
        return redirect("/")
    return render_template("user/login.html")

#로그인 처리 라우터
@user_bp.route("/login", methods=["POST"])
def loginok() :
    id = request.form.get("id")
    pw = request.form.get("pw")

    # db에서 id,pw에 일치하는 회원 조회
    dao = UserDAO()
    user = dao.login(id,pw)

    # 있으면? session에 데이터 저장
    if user :    #if user is not None
        session["user"] = user
        return redirect("/")  # 메인 redirect
    # 없으면? 로그인 redirect
    return redirect("/user/login")

#회원정보수정 화면 라우터
@user_bp.route("/modify", methods=["GET"])
def modify() :
    # 로그인 했으면?
    user = session.get("user")

    #로그인 안했으면?
    if not user :
        #로그인 화면으로 redirect
        return redirect("/user/login")
    #user = {id : "hong", nick : "hgd", pw : "1234"}
    #id, pw, nick = user.values()
    id = user["id"]
    pw = user["pw"]
    nick = user["nick"]

    # session에서 id 꺼내서 db에서 회원정보조회 템플릿에 전송

    return render_template("user/modify.html", id=id, pw=pw, nick=nick)


#회원정보수정 처리 라우터
@user_bp.route("/modify", methods=["POST"])
def modifyok() :
    #get,post 모두 로그인이 필요한 경우에는 session유무 검사가 필요
    id = session.get("user").get("id")
    pw = request.form.get("pw")
    nick = request.form.get("nick")
    
    #db에서 업데이트 처리
    dao = UserDAO()
    cnt = dao.modify(id, pw, nick)

    #업데이트됐다면 session에도 업데이트
    if cnt :
        #session["user"]["id"] = id
        #session["user"]["pw"] = pw
        #session["user"]["nick"] = nick
        session["user"] = {
            "id" : id,
            "pw" : pw,
            "nick" : nick
        }
    return redirect("/user/modify")

#로그아웃 처리 라우터
@user_bp.route("/logout", methods=["POST"])
def logout() :
    #세션에 저장된 정보를 삭제
    #del session["user"]
    session.pop("user", None) #.get은 읽기전용 대체가 안됨
    return redirect("/user/login")

#탈퇴 처리 라우터
@user_bp.route("/leave", methods=["POST"])
def leave() :
    #세션에 저장된 id 꺼내서 delete쿼리
    id = session.get("user").get("id")
    dao = UserDAO()
    dao.leave(id)

    #세션 삭제
    session.pop("user", None)
    return redirect("/")
