#템플릿 렌더링
#jinja 템플릿엔진
#서버에서 html로 데이터를 전달
#html에서 조건문, 반복문을 이용해 화면을 동적 렌더링
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home() :
    return render_template(
        "jinja.html",
        name="홍길동",
        time=datetime.datetime.now(),
        age=20,
        gender="M",
        height=178.2,
        boole=True
    )

@app.route("/weather/<condition>")
#localhost:5000/weather/
def weather(condition) : #동적라우팅은 함수의 파라미터로 값을 받아줘야한다
                            #여러개도 가능
    return render_template("weather.html", weather=condition)

@app.route("/todo")
def todo() :
    todos = ["공부하기", "책읽기", "flask 공부하기"]
    todos = [
        {
            "title" : "제목1",
            "body" : "본문1",
            "author" : "hong"
        },
        {
            "title" : "제목2",
            "body" : "본문2",
            "author" : "jeon"
        }
    ]
    return render_template("todo.html", todos=todos)
app.run(debug=True)


#서버사이드 렌더링
#natural 템플릿