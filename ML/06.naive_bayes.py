# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 15:22:44 2025

@author: MYCOM

msg = "나는 오늘 학교에 가서 공부를 열심히 했다."
okt = Okt()    #클래스

# 문장의 모든 품사를 추출한다.
item = okt.morphs(msg)
print(item)

# 문장의 모든 단어와 품사정보를 추출한다.
item = okt.pos(msg)
print(item)

# 문장에서 명사만 추출한다.
item = okt.nouns(msg)
print(item)
"""
import warnings
warnings.filterwarnings("ignore")
#나이브베이즈 분류기를 이용한 문서분류

#형태소 분석


#형태소 분석기 설치
# conda install -c conda-forge jpype1
# pip install konlpy

import pandas as pd
from konlpy.tag import Okt

df = pd.read_excel("nv_data.xlsx")
print(df)
print("--" * 25)

#감정 데이터를 그풉핑해서 표시한다.
group = df.groupby("감정")["감정"].unique()
print(group)
print("--" * 25)

#형태소 분석 후 토큰화(명사위주의 )
#형태소 분석기 객체를 생성한다.
okt = Okt()

total_rows = len(df)
print(f"전체행 : {total_rows}")
print("--" * 25)

emotion = df.iloc[0]["감정"]
text = df.iloc[0]["문장"]
print(emotion, "==>", text)
print("--" * 25)

train = []
for row in range(total_rows):
    emotion = df.iloc[row]["감정"]
    text = df.iloc[row]["문장"]
    print(f"{emotion} ==> {text}")
    
    #문장에 대해서 형태소 분석을 수행한다.
    #tokens = okt.nouns(text) # 명사만 추출
    tokens = okt.morphs(text) # 모든 품사 추출
    print(tokens)
    #나이브베이즈 학습을 위한 데이터를 가공한다.
    #원핫 인코딩을 위한 전처리
    """
    #원래 데이터
    슬픔,A B C
    기쁨,D E F
    """
    """
    #학습용 데이터로 가공
    [
        (["A", "B", "C"], "슬픔"),
        (["D", "E", "F"], "기쁨")
    ]
    """
    train.append((tokens, emotion))
print("--" * 25)

#학습용 데이터 출력
print(train[0], train[1])
print(train[0:3])

"""
#전체 키워드를 원핫인코딩 방식의 데이터셋으로 변환
tokens(전체 키워드) : A, B, C, X, Y, Z
train(학습대상 문서)
[ 
    ( ["A", "B", "C"], "슬픔"), 
    ( ["X", "Y", "Z"], '분노') 
]
train_xy(학습용 데이터)
[ 
    ( {"A" : True, "B" : True, "C" : True,"X" : False, "Y" : False, "Z"  : False }, "슬픔"), 
    ( {"A" : False, "B" : False, "C" : False,"X" : True, "Y" : True, "Z" : True }, '분노') 
]

data = [ ("봄", "11"), ("여름", "22"), ("가을", "33"), ("겨울", "44")]
print([ v[0] for v in data])

"""







#학습용 데이터 생성



#나이브베이즈 학습

#문장테스트

#명사만 추출해 학습하면 제대로 된 결과를 얻을 수 없다

"""

[for v in train]


tokens = set()
arr = [ tokens.add(t) for v in train for t in v[0]]
print(arr)


doc = [1, 2, 3, 1]
print(set(doc))



















tokens = [ t for v in train for t in v[0] ]
tokens = set(tokens)
tokens = list(tokens)
tokens.sort()
print(tokens)

#학습용 데이터 생성
#tokens = [A,B,C,D]
#doc = [A,B,A,B]
#return <- { A : True, B : True, C : False, D : False}
def term_exists(doc):
    return {word : (word in set(doc)) for word in tokens}

train_xy = [(term_exists(token), emotion) 
            for token,emotion in train]    
print(train_xy)    
print("=" * 30)


#나이브베이즈 학습
import nltk

model = nltk.NaiveBayesClassifier.train(train_xy)

#문장테스트
msg = "회의 중에 사장님이 욕을 하셨어."
msg = "회사 분위기가 너무 좋아"
msg = "퇴사 후 새로운 회사에 이직하려고 면접을 봤는데 연락이 없어."
msg = ""
#학습했던 데이터와 동일한 형태의 데이터형식 필요

sentence = term_exists(okt.nouns(msg))
sentence = term_exists(okt.morphs(msg))
#print(sentence)

result = model.classify(sentence)
print("분류결과 :", result)
print("=" * 30)

#명사만 추출해 학습하면 제대로 된 결과를 얻을 수 없다
"""