#pandas
#Panel data

#데이터 분석과 처리를 위한 파이썬 라이브러리
#데이터를 쉽게 불러오고, 정리하고, 분석할 수 있다.
#머신러닝/딥러닝을 위한 데이터 전처리에 필수적

#데이터 전처리
#결측값 대체, 삭제 / 수집한 데이터의 타입을 변환

#판다스의 데이터 구조
#1. 시리즈(Series)
#1차원 데이터구조, 인덱스를 포함한 배열 형태
#index-value 구조

#2. 데이터프레임(DataFrame)
#2차원 데이터구조, 행과 열을 포함한 데이터
#행-렬 구조
import pandas as pd

#1. 시리즈 생성
s = pd.Series([1,2,3,4])
print(s) # 헤더(데이터의 라벨?)가 없다
#0 ~ 3번 인텍스에 1 ~ 4의 값

print(s.index)
#시리즈의 인덱스 정보
#RangeIndex(start=0, stop=4, step=1)
#0인덱스에서 3까지 1계단씩 증가하는 인덱스범위를 가지고 있다
print(s.values)
#시리즈의 값 정보(넘파이 배열 형태)
#[1 2 3 4]

print(s.dtype)
#시리즈의 데이터 타입
s = pd.Series([1,2,3,4], index=["a", "b", "c", "d"])
print(s)


dict = {
    "홍길동" : "a팀",
    "전우치" : "b팀",
    "성춘향" : "c팀",
    "김철수" : "c팀",
}

s = pd.Series(dict)
print(s)
#리스트, 딕셔너리, 넘파이배열 등을 사용하여 시리즈 생성 가능
#인덱스를 지정하지 않으면 0부터 시작하는 정수 인덱스가 자동 할당

#시리즈의 인덱싱과 슬라이싱
print(s["홍길동"])
print(s["김철수"])
#결과가 값으로 반환

print("-" * 30)
print(s[["홍길동", "김철수"]])
#결과가 시리즈로 반환
print("-" * 30)

print(s.iloc[1])
#정수위치(행번호)를 사용하여 데이터에 접근

dict = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4
}

s = pd.Series(dict)
print(s)
# "a" ~ "d" 인덱스, 1 ~ 4 값

print(s["a"])
s["a"] = "5"
print(s)
s["a"] = 5
print(s)

print("-" * 30)
print(s.dtype)
s = s.astype(int)      
 #문자열을 정수로 변환하면서 dtype을 int로 변경
print(s.dtype)

s = pd.to_numeric(s, errors="coerce").astype("Int64")
# 숫자로 변환할 수 없는 값은 NaN으로 안전하게 처리
print(s.dtype)
print("-" * 30)

s["e"] = 8
print(s)

#print(s["f"])
#없는 인덱스에 접근하면 에러

#시리즈 내에서 데이터            /검색/
print(s > 0)        #시리즈 S의 value가 0보다 큰 인덱스를 찾아 true 표시
                    #조건에 충족되지 않는 나머지 value는 false

print((s > 5).all)  #시리즈 s의 모든 value가 5보다 큰가

#반환된 결과를 인덱스 조회에서 사용가능 



#불리언 인덱싱      아래는 조회
print(s[[True, True, True, True, True]])
print(s[[True, False, True, False, True]])
print(s[s >= 4])


print(s.where(s > 2))
#시리즈 s의 value가 2보다 큰 값은 그대로 / 나머지는 NaN

#인덱스 0부터 5까지 2step으로 시리즈 생성(0, 2, 4 의 3원소)
s2 = pd.Series([10, 20, 30], index=range(0, 6, 2))
print(s2)
print(s2.index)

