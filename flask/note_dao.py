#notes테이블에 접근해서 쿼리를 수행하는 클래스
import pymysql

class NoteDAO :
    def __init__(self) :
        #연결객체?
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="ezen",
            database="flask_db",
            cursorclass=pymysql.cursors.DictCursor
        )
    
        #쿼리실행 객체
        self.cursor = self.conn.cursor()
    
    #게시글 목록 조회 함수
    def notes(self) :
        sql = "select * from notes"
        self.cursor.execute(sql)
        notes = self.cursor.fetchall()  #결과 : [{}, {}]  /  없음 : []
        self.close()
        return notes

    #게시글 단건 조회 함수
    def note(self, no) :
        sql = "select *from notes where no = %s"
        self.cursor.execute(sql, (no,))
        note = self.cursor.fetchone() #없으면 : None
        self.close()
        return note
    
    #게시글 작성 함수
    def write(self, title, content, id) :
        sql = "insert into notes(title, content, author) values(%s, %s, %s)"
        self.cursor.execute(sql, (title, content, id))
        self.conn.commit()

        #마지막에 insert되어 commit된 auto_increment값
        no = self.cursor.lastrowid
        self.close()
        return no

    #게시글 수정 함수
    def modify(self, title, content, no) :
        sql = "update notes set title = %s, content = %s where no = %s"
        self.cursor.execute(sql, (title, content, no))
        self.conn.commit()
        #result = self.cursor.rowcount
        self.close()

    #게시글 삭제 함수
    def delete(self, no) :
        sql = "delete from notes where %s"
        self.cursor.execute(sql, (no,))
        self.conn.commit()
        self.close()

    #db연결 종료 함수
    def close(self) :
        self.cursor.close()
        self.conn.close()
