# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 10:13:38 2025

@author: MYCOM
"""
#텍스트 마이닝, 텍스트 전처리
#텍스트 마이닝 : 비정형 텍스트 데이터를 분석하여 의미있는 정보를 추출하는 과정

#텍스트 마이닝의 과정
#1. 데이터 수집 : 크롤링
#2. 텍스트 전처리 : 특문제거, 대소문자 변환, 공백 제거, 불용어(용도가 없는)제거
#3. 토큰화 : 문장을 단어단위로
# > 제 이름은 홍길동 입니다. > ['제', '이름은', '홍길동']
# > 이렇게 해야 단어가 얼마나 많이 등장했는지 등등 의 분석이 가능
#4. 형태소 분석 : 이름은 > 이름 + 은
#5. 불용어제거 : 사용하지 않는 단어 제거 (은, 는, 이, 가, 등등)
#6. 시각화(워드클라우드)
#7. 감성 분석 : 라벨링이 되어 있어야 한다.

#OKT
from konlpy.tag import Okt

okt = Okt()
# =============================================================================
# 형태소 분석 
text = "텍스트 마이닝을 활용한 데이터 분석이 재밌다!"
print(okt.morphs(text))

#품사태깅
print(okt.pos(text))
#noun,verb,adjective,josa,punctuation
#명사,동사,형용,조사,문장부호

#명사만 추출
print(okt.nouns(text))

#어간 추출
#언어의 원형태
#단어(동사)의 원형(어간)을 찾아줌(stem)
okt.morphs("먹을것이다", stem=True)
# =============================================================================

#1. 텍스트 전처리
import pandas as pd
df = pd.read_csv("naver_news_data.csv")

content = df["내용"]
# =============================================================================
# l = ["a", "b", "c", "d"]
# s = ","
# s.join(l)
# == "a,b,c,d"
# " ".join(l)
# == "a b c d"
# =============================================================================
text = " ".join(content)
#print(text[:2000])

#nvidia, 엔비디아  이런경우의 처리

#정규표현식 특수문자 제거
#분량이 방대함
import re #
#re.sub(r"[ㄱ]", text) # text에서 ㄱ제거
#re.sub(r"[^가-힣]\s", "", text) # text에서 ㄱ제거
#text변수에서 가, 나, 갸, 거, ..., 힣 까지 와 공백은 제외
# 그 외는 모두 ""으로 치환
#\s : 문자 뒤의 string하나 포함하고????
text = re.sub(r"[^가-힣\s]", "", text) 
#print(text)

#2.토큰화 + 형태소분석
words = okt.morphs(text, stem=True)
#words = okt.nouns(text)
print(words)

#3. 불용어 제거
#한국어 불용어 
stopwords = ['에는', '아니다', '이라고', '따르다', '부터', '보다', '늘다', '않다', '만', '돼다', '까지', '하고', '되다', '다', '인', '이다', '로', '에서', '으로', '있다', '에', '의', '하다', '와', '과', '고', '을', '를', '도', '었', '이', '있', '하', '것', '들', '그', '되', '수', '이', '보', '않', '없', '나', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대해', '오', '말', '일', '그렇', '위하', '은', '는', '가']

filtered_word = [word for word in words if word not in stopwords]
print(filtered_word)
"""
filter_words = []
for word in words :
    if word not in stopwords :
        filter_words.append(word)
"""

#4. 분석
from collections import Counter
word_count = Counter(filtered_word)
print(word_count.most_common(10))  #word 리스트에서 가장 많이 등장한 단어 10개

common_word_count = word_count.most_common(100)
#[(단어,개수),(단어,개수), ..., 100개]
print(dict(common_word_count))

#5. word cloud 시각화
#pip install wordcloud
from wordcloud import WordCloud
wordcloud = WordCloud(
    font_path="malgun.ttf",
    background_color="white",
    width=800,
    height=600
).generate_from_frequencies(dict(common_word_count))

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.show()


