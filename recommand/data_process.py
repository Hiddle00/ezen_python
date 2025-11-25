#한국 영화데이터 전처리 파일
#결측치 제거, 채움, 특정 장르 제거....
import pandas as pd
df = pd.read_csv("kmdb_movie_list.csv")
print(df.info())

#영화의 제목만 결측값 제거
df = df.dropna(subset=["title"])

#필요한 컬럼들을 빈문자로 치환
df["genre"] = df["genre"].fillna("")
df["director"] = df["director"].fillna("")
df["actorNm"] = df["actorNm"].fillna("")
df["plot"] = df["plot"].fillna("")
df["keywords"] = df["keywords"].fillna("")

#장르 필터링
#포함 되어있다면 True / x = False
df = df[~df["genre"].str.contains("에로")]
print(df.info())



#추천에 사용할 컬럼을 하나의 문자열로 합쳐서 새로운 컬럼을 생성
df["features"] = df["title"] + " " + df["director"] + " " + df["genre"] + " " + df["actorNm"] + " " + df["plot"] + " " + df["keywords"]

#features 컬럼에서 데이터 전처리
df["features"] = df["features"].str.strip().replace(r"[^가-힣a-zA-Z0-9\s]", "", regex=True)
#r"[가-힣a-zA-Z0-9\s]" 정규 표현식으로 해당 문자를 모두 찾는다
#^ : 해당 문자열 제외
#2번 파라미터 : ""로 치환
#regex : 

df.to_csv("movie_list_cleaned.csv", index=False)