from flask import request, render_template, redirect, session, Blueprint
from note_dao import NoteDAO
#노트 관련 라우터(controller)
note_bp = Blueprint("note", __name__, url_prefix="/notes")

"""
글쓰기
    -> 화면 /write, GET
    -> 처리 /write, POST, insert, title, content, redirect 글상세
글수정
    -> 화면 /notes/modify/3 <-> notes/3/modify, GET
    -> 처리 /notes/3/modify, POST, update, title, content, redirect /notes/3
글삭제
    -> 처리
글목록
    -> 화면
글상세
    -> 화면
"""
#글쓰기 화면 라우터
@note_bp.route("/write", methods=["GET"])
def write() :
    if session.get("user").get("id") :
        return render_template("note/write.html")
    return render_template("note/list.html")

#글쓰기 처리 라우터
@note_bp.route("/write", methods=["POST"])
def writeok() :
    title = request.form.get("title")
    content = request.form.get("content")
    user = session.get("user")
    id = user.get("id")
    
    #NoteDAO생성자 호출, 사용자 입력값을 파라미터로 넘겨 insert
    dao = NoteDAO()
    no = dao.write(title, content, id)
    return redirect(f"/notes/{no}")

#글목록 화면 라우터
@note_bp.route("/", methods=["GET"])
def notes() :
    #select *from notes;
    dao = NoteDAO()
    notes = dao.notes()
    return render_template("note/list.html", notes=notes)

#글상세 화면 라우터
#가변 라우팅의 파라미터에는 타입을 알려줄 수 있다
@note_bp.route("/<int:note_no>", methods=["GET"])
def note(note_no) :
    #select *from notes where no = 1;     문자열이면 pymysql이 '1'식으로 처리
    dao = NoteDAO()
    note = dao.note(note_no)
    #print(note)
    if not note :
        return redirect("/notes")    #없는 게시글(note==None)을 조회하면 목록으로 빠짐
    return render_template("note/view.html", note=note)

#글수정 화면 라우터
@note_bp.route("/<int:note_no>/modify", methods=["GET"])
def modify(note_no) :
    dao = NoteDAO()
    note = dao.note(note_no)
    if not note :
        return redirect("/notes")
    return render_template("note/modify.html", note=note)

#글수정 처리 라우터
@note_bp.route("/<int:note_no>/modify", methods=["POST"])
def modifyok(note_no) :
    title = request.form.get("title")
    content = request.form.get("content")
    dao = NoteDAO()
    dao.modify( title, content,no = note_no)
    return redirect(f"/notes/{note_no}")

#글삭제 처리 라우터
@note_bp.route("/<int:note_no>/del", methods=["POST"])
def delete(note_no) :
    #로그인 했는지, 게시글의 작성자가 로그인한 사용자와 동일한지
    user = session.get("user")
    if not user :
        return redirect("/notes")
    
    dao = NoteDAO()
    note = dao.note(note_no)
    if not note :
        return redirect("/notes")
    
    if user["id"] != note["author"] :
        return redirect("/notes")

    dao = NoteDAO()
    dao.delete(note_no)
    return redirect("/notes")



"""
http method

GET
POST
UPDATE
DELETE
"""