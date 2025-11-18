#파일 업로드
import os

print(os.path)   #작업 경로

#현재 작업 경로에 templates폴더나 파일이 있는지 확인
print(os.path.exists("templates"))

#uploads폴더 생성
#os.makedirs("uploads")

#print(os.path.join("uploads", "a.jpg"))
#개발 os에 맞게 경로를 조합
#windows : uploads\a.jpg
#linux/mac : uploads/a.jpg

from flask import Flask, request, render_template
import uuid
app = Flask(__name__)

#파일 업로드 경로가 현재폴더\uploads\파일
#경로가 없으면 나는 에러를 대응()
if  not os.path.exists("uploads") :     #없으면 True / 있으면 False
    os.makedirs("uploads")

@app.route("/")
def home() :
    return render_template("upload.html")
#localhost:5000로 접속하면 templates/upload.html파일을 반환

@app.route("/upload", methods=["POST"])
def upload() :
    #print(request.files)
    #ImmutableMultiDict([('file', <FileStorage: '' ('application/octet-stream')>)])
    #name : 키
    file = request.files["file"]
    #request.files.get("file")    #dict여서 get으로 꺼낼수 있다.
    #if가 실행 안되는 조건
    #False, "", 0, , None, [], {}, ...
    if file :
        print(file)
        print(file.name)
        print(file.content_type)
        print(file.content_length)   #메타데이터

        print(file.filename)
        print(file.mimetype)
    if file :
        file_path = os.path.join("uploads", file.filename)
        #uploads\파일이름
        file.save(file_path)
        return "파일 업로드 성공"
    return "파일 업로드 실패"

@app.route("/multi-upload", methods=["POST"])
def multi_upload() :
    files = request.files.getlist("file")

    if not files :
        return "파일을 업로드 해주세요"
    for file in files :
        ext = os.path.splitext(file.filename)[1]
        file_name = uuid.uuid4()
        #a.txt -> ["a", ".txt"]
        #03.a.py -> ["03.a", ".py"]
        file_path = os.path.join("uploads", f"{file_name}{ext}")
        file.save(file_path)
    return "파일 업로드 완료"
app.run(debug=True)  #port=8080
