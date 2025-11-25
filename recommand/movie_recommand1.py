import pandas as pd
df = pd.read_csv("movie_list_cleaned.csv")
print(df.info())

df = df.fillna("")
#텍스트를 숫자로 변환(벡터화)
#BOW(Bag Of Words) 벡터화 : 범주형 데이터를 솎아낼때 주로 사용
#각 단어들을 고유 숫자로 대체
#ex. 여호 = 0, 여우 = 1

#TF-IDF(Term Frequency - Inverse Document Frequency) 벡터화
#등장 횟수에 대한 가중치가 있음(tf)
#전체 문서에 적은 단어를 가중치를 높임(idf)
#너무 많이 등장하는 단어는 가중치를 낮춤

from sklearn.feature_extraction.text import TfidfVectorizer

#tf-idf 벡터화
#모든 문서에 단어가 하나 등장해도 벡터화(빠짐없이 모든 단어포함 : min_df=1)
#1-gram, 2-gram, 3-gram, ... , n-gram
#단어 하나와 여러단어(유니그램,빅그램?)
#1-gram과 2-gram을 사용
"""

"""
tfidf = TfidfVectorizer(min_df=1, ngram_range=(1, 2))
#하이퍼파라미터
#단어가 한 번 등장하는 것도 취급, 두 개의 단어를 묶어서 벡터화

#실제 벡터화
matrix = tfidf.fit_transform(df["features"][:100])
#해당컬럼만(title, features, 등)
#행렬로 변환
#df에서 특정 컬럼을 가져와야함
print(matrix)
#단어수 가중치
#90000행에 각 행별로 입력된 단어들의 벡터화 결과
print(matrix.toarray())
#벡터화에 사용된 각 단어 특성들
print(tfidf.get_feature_names_out()) # 실제 단어 뭉치

# 제목만 dow벡터화 했을 때 단어마다 고유 숫자로 대체
# tfidf는 


from sklearn.metrics.pairwise import cosine_similarity
#영화(제목)끼리의 관계를 만든다

#코사인 유사도
#sim_scores : 유사도 행렬(90,000 x 90,000) (행, 열)
#tf-idf벡터들의 내각(cos)을 일일히 비교
sim_scores = cosine_similarity(matrix, matrix)
print(sim_scores)

#특정 영화에 대한 유사도를 보고 싶다면 해당 영화의 행 인덱스를 구해야함
#해당 영화의 점수?
target = " 컨저링 하우스"
#title컬럼의 값이 "컨저링 하우스"인 행 인덱스 조회
target_index = df[df["title"] == target].index[0]
#해당 영화의 index

print(target_index)
print(sim_scores[target_index])  #해당 영화의 유사도 결과
#유사도 행렬에서 4번 인덱스("컨저링 하우스")영화에 대한 유사도를 조회

#리스트를 내림차순 정렬하기위해 시리즈로 생성(np.sort해도 되지만 더 길수있다?)
scores = pd.Series(sim_scores[target_index])
#4번 영화에 대한 유사도 리스트를 내림차순으로 정렬
sorted_scores = scores.sort_values(ascending=False)
"""
인덱스 유사도
4 1
3 0.01
"""
print(sorted_scores)

#유사도 리스트에서 인덱스를 1번 ~ 4번까지 슬라이싱
#[3, 1, 2, 5]
top_indexes = sorted_scores.index[1:5]  #인덱스화 된 점수
#유사도 리스트에서 유사도 점수를 1번 ~ 4번까지 슬라이싱
#[0.01, 0, 0, 0]
top_scores = sorted_scores.iloc[1:5]  #실제 점수

#유사도 리스트에서 구한 유사한 영화의 인덱스 상위 4개를 이용해서
#원본 데이터프레임에서 데이터를 조회
result = df.iloc[top_indexes]

print(result[["title", "genre", "plot"]])


# 전처리 시 새로운 컬럼에 모든 값을 다 집어넣고 학습?
# 