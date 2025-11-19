#users테이블에 접근해서 쿼리를 실행하는 클래스
#회원가입
#로그인
#회원정보수정
#회원탈퇴

import pymysql
"""
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen"
    database="flask_db"
)

cursor = conn.cursor()
sql = "insert into users(id, pw, nick) values(%s, %s, %s)"

cursor.execute(sql, ())
"""
class UserDAO :
    def __init__(self):
        #dao클래스의 생성자
        #생성자가 호출될 때 db에 연결, cursor 생성
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="ezen",
            database="flask_db",
            cursorclass=pymysql.cursors.DictCursor
            #[(),()] -> [{},{}]
            #조회 결과를 받을때만 영향있음
        )
        self.cursor = self.conn.cursor()

    #아이디 중복체크
    def id_check(self,id) :
        sql = "select count(*) as cnt from users where id = %s"
        self.cursor.execute(sql, (id))
        result = self.cursor.fetchone()
        #[(count(*), 1), ()]
        #fetchall -> 2차원 반환 / 꺼낼때 result[0]["cnt"]
        return result.get("cnt")
    
    #회원가입 함수
    def join(self,id,pw,nick) :
        sql = "insert into users(id, pw, nick) values(%s, %s, %s)"
        self.cursor.execute(sql, (id, pw, nick))
        self.conn.commit()
        self.close()

    #로그인 함수
    def login(self, id, pw) :
        sql = "select * from users where id = %s and pw = %s"
        self.cursor.execute(sql, (id, pw))
        result = self.cursor.fetchone()
        self.close()
        return result
    
    #회원정보 수정
    def modify(self, id, pw, nick) :
        sql = "update users set pw = %s, nick = %s where id = %s"
        self.cursor.execute(sql, (pw, nick, id))
        self.conn.commit()
        result = self.cursor.rowcount
        self.close()
        #쿼리가 실행됨으로 인해 영향을 받은 행의 개수
        return result
    
    #회원탈퇴
    def leave(self, id) :
        sql = "delete from users where id = %s"
        self.cursor.execute(sql, (id,))
        self.conn.commit()
        self.close()
    
    #자원 회수
    def close(self) :
        self.cursor.close()
        self.conn.close()

    