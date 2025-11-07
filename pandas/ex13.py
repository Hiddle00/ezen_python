# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 09:19:43 2025

@author: MYCOM
"""
#pandas + matplotlib
#pandas : 데이터 전처리(결측치,필요없는데이터)
import pandas as pd
import matplotlib.pyplot as plt

#1. 데이터(csv파일)로드
df = pd.read_csv("AB_NYC_2019.csv")
#2019년 뉴욕에 영업중인 AirBnB 업장
#강제로 모든 행을 출력하려면 반복문으로 해야한다
#print(df)

#데이터의 기본 탐색
print(f"데이터의 크기 : {df.shape}")
#48,895행, 16열

print(f"컬럼 목록 : {df.columns}")

"""
아이디, ~ , 지역구, ~ , 위경도
'id', 'name', 'host_id', 'host_name', 'neighbourhood_group'주,
       'neighbourhood'세부구역, 'latitude'위도, 'longitude', 'room_type', 'price' 1박/$,
       'minimum_nights', 'number_of_reviews', 'last_review',
       'reviews_per_month', 'calculated_host_listings_count',
       'availability_365'
"""
print("--" * 25)

#데이터 샘플(상위 5개 행)
print(df.head())
print(df[["name", "price"]])
print("--" * 25)

#데이터 구조 출력
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 48895 entries , 0 to 48894
            #행              #인덱스
Data columns (total 16 columns):
 #   Column                          Non-Null Count  Dtype  
---  ------                          --------------  -----  
 0   id                              48895 non-null  int64  
                                     공백X
 1   name                            48879 non-null  object 
                                     결측치
 2   host_id                         48895 non-null  int64  
 3   host_name                       48874 non-null  object 
 4   neighbourhood_group             48895 non-null  object 
 5   neighbourhood                   48895 non-null  object 
 6   latitude                        48895 non-null  float64
 7   longitude                       48895 non-null  float64
 8   room_type                       48895 non-null  object 
 9   price                           48895 non-null  int64  
 10  minimum_nights                  48895 non-null  int64  
 11  number_of_reviews               48895 non-null  int64  
 12  last_review                     38843 non-null  object 
 13  reviews_per_month               38843 non-null  float64
 14  calculated_host_listings_count  48895 non-null  int64  
 15  availability_365                48895 non-null  int64  
dtypes: float64(3), int64(7), object(6)
memory usage: 6.0+ MB
None
"""
print("--" * 25)

#수치형 데이터 기초통계량(통계형 데이터를 보여줌)
print(df.describe())
#열이 길어서 모두 볼 수 없음
print(df["price"].describe())
"""
[8 rows x 10 columns]
count    48895.000000
mean       152.720687
                  평균
std        240.154170
              표준편차
min          0.000000
25%         69.000000
50%        106.000000
                중간값
75%        175.000000
max      10000.000000
            최대값 1만$ ㄷㄷ
Name: price, dtype: float64
"""

#범주형 데이터 개수 확인(범주는 기초통계가 불가능. int타입이어도 카테고리의 개수에 관련된 데이터기 때문에 잘못된 통계생성)
#객실 유형별 데이터 개수
print(df["room_type"])
print(df["room_type"].value_counts())

#pd.set_option("display.max_columns", None)
#컬럼(열) 출력 제한 해제
print(df.sample(5))
#랜덤으로 5개의 샘플데이터를 추출


#분석 결과
#약 49,000개의 행, 16개의 열
#컬럼 이름, 데이터타입
#실제 데이터의 구성정보
#대략적인 결측치 확인(name컬럼 16개, 등등)
#대략적인 이상치 확인(price컬럼 1만$, 0$, 등등)


#데이터 전처리
#2-1. 컬럼이름변경(영어 -> 한국어)
#df.columns = ["A", "B", ...]
#기존 컬럼 순서와 개수에 맞게 대입

#id, name, host_id, host_name
columns_dict = {
    "id" : "아이디", "name" : "이름", "host_id" : "호스트아이디",
    "host_name" : "호스트이름",
    "neighbourhood_group" : "지역구", 'neighbourhood': '세부지역',
    'latitude': '위도', 'longitude': '경도',
    'room_type': '방유형', 'price': '가격',
    'minimum_nights': '최소숙박일수',
    'number_of_reviews': '리뷰수',
    'last_review': '최근리뷰날짜',
    'reviews_per_month': '월평균리뷰수',
    'calculated_host_listings_count': '호스트리스트개수',
    'availability_365': '연중이용가능일수'
}
df.rename(columns = columns_dict, inplace=True)
print(df.info())
print("--" * 25)

#2-2. 결측치 처리
#fill(0등으로 대체), mean(평균치)
#월평균리뷰수 컬럼의 결측치를 0으로 대체
#df["월평균리뷰수"].fillna(0, inplace=True)
df["월평균리뷰수"] = df["월평균리뷰수"].fillna(0)

#이름, 호스트이름 컬럼의 결측치는 "정보없음"으로 대체
df["이름"] = df["이름"].fillna("정보없음")
df["호스트이름"] = df["호스트이름"].fillna("정보없음")

"""
print(df["최근리뷰날짜"])
#행에 리뷰점수가 있는데 NaN이면 문제있는 값

#리뷰가 없는 숙소는 월평균 리뷰수도 0으로 대체
print(df["리뷰수"] == 0)
print(df["월평균리뷰수"].isnull())
"""

#최근리뷰날짜가 null인 행을 제거
df = df.dropna(subset=["최근리뷰날짜"])

#리뷰가 없는 숙소는 월평균 리뷰수도 0으로 설정
#최근리뷰날짜가 null인 행은 리뷰가 있는 경우에는 임의의 날짜로 대체
#결측치에 대해서 같은 지역구의 평균값으로 대체
#pdf참고

print(df.info())
print("--" * 25)

#2-3. 이상치 탐지 및 제거
print((df["가격"] <= 0).sum())
#숙박료가 0$ 이하인 데이터가 10개

print((df["가격"] >= 1000).sum())
#숙박료가 1,000$ 이상인 데이터가 137개

#숙박료가 0$를 초과하고 1000$미만인 데이터를 조회
print(((df["가격"] > 0) & (df["가격"] < 1000)).sum())

#숙박료가 0$이하이고, 1000$이상인 데이터를 제거
#숙박료가 0$초과이고, 1000$미만인 데이터를 새로운 df에 대입
df = df[(df["가격"] > 0) & (df["가격"] < 1000)]
print(df.info())

#최소숙박일수가 0일 이하인 데이터의 개수 조회
print((df["최소숙박일수"] <= 0).sum())
#최소숙박일수가 40일 이상인 데이터의 개수 조회
print((df["최소숙박일수"] >= 40).sum())
print("--" * 25)

#최소숙박일수가 40일 이상인 데이터를 제거
#최소숙박일수가 40일 미만인 데이터를 이용해서 df를 조회하고 결과값을 원본에 대입
df = df[df["최소숙박일수"] < 40]
print(df.info())
print("--" * 25)

#연중이용가능 일수가 0일 이하인 데이터의 개수 조회
print((df["연중이용가능일수"] <= 0).sum())
#연중이용가능 일수가 365일인 데이터의 개수 조회
print((df["연중이용가능일수"] == 0).sum())
print("--" * 25)

#연중이용가능 일수가 0일 초과인 데이터를 이용해 df를 조회 후 원본 df에 대입
df = df[df["연중이용가능일수"] > 0]
print(df.info())
print("--" * 25)
print(df)

#2-4. 중복데이터 처리
#중복데이터 확인
#df내에서 모든 컬럼의 값이 중복된 행의 개수
print(df.duplicated().sum())
#df내에서 아이디 컬럼의 값이 중복된 행의 개수
print(df["아이디"].duplicated().sum())
#
print(df[df.duplicated()])

#중복데이터 제거
#모든 컬럼을 비교해 중복 제거
df = df.drop_duplicates()
#아이디 컬럼을 비교해 중복 제거
df = df.drop_duplicates(subset=["아이디"])
#두컬럼을 기준으로 제거도 가능

#2-5. 데이터 변환
#가격과 최소숙박일수를 곱해서 최소비용 컬럼생성
df["최소비용"] = df["최소숙박일수"] * df["가격"]
print(df.info())
print(df["최소비용"])
print(df[["최소숙박일수", "가격", "최소비용"]])

def c(price) :
    if price >= 500 :
        return "럭셔리"
    return "스탠다드"
#가격분류 컬럼을 생성하고 가격이 500$ 이상이면 럭셔리, 아니면 스탠다드
df["가격분류"] = df["가격"].apply(c)
print(df.info())
print(df)
print(df[["가격", "가격분류"]].tail(10))


#3. 데이터 시각화
#연중 이용가능일수
plt.hist(df["연중이용가능일수"])
plt.show()

#지역구별 리스팅 수 시각화
print(df["지역구"].value_counts())
print(df["지역구"].value_counts().index)
print(df["지역구"].value_counts().values)

region = df["지역구"].value_counts()

plt.bar(region.index, region.values)
plt.show()

df["지역구"].value_counts().plot(kind="bar")
plt.show()

# "지역구별 평균가격" 시각화

print(df.groupby("지역구")["가격"].mean())
avg = df.groupby("지역구")["가격"].mean()

avg.index #[맨하탄, 브루클린, ...]
avg.values #각 지역구별 평균 가격
plt.bar(avg.index, avg.values)







