#훈련용 데이터 세트와 테스트용(시험용)
#데이터 세트 분리 연습

import pandas as pd

# iris.csv 파일을 읽어 들인다.


try:
    df = pd.read_csv("iris.csv")
    print(df.head(3))   #dataframe
    print("=" * 30)
except Exception:
    print("읽기 오류")

# 열이름으로 데이터를 출력하기
print(df["species"])
print("=" * 30)

# species 열을 그룹핑해서 보여주기
print(df.groupby("species").size())
print("=" * 30)

# 데이터 인코딩 : 문자열 카테코리를 숫자로 변환
# setosa => 0 / versicolor => 1 / virginica => 2
species = ["setosa", "versicolor", "virginica"]
for i in range(0,len(species)) :
    #print(species[i])
    df["species"] = df["species"].str.replace(species[i],str(i))

print(df.head())
print("-" * 30)

# encoding된 데이터프레임을 iris_encode.csv로 저장
df.to_csv("iris_encode.csv")

# 총 150개 데이터를 7:3으로 나눈다
from sklearn.model_selection import train_test_split

# 독립변수(X)와 종속 변수(y)를 분리한다.

#종속 변수(y)
y = df["species"]
print(y)
print("=" * 30)

# 독립 변수(X : sepal_length, sepal_width, petal_length, petal_width)
X = df[ ["sepal_length", "sepal_width", "petal_length", "petal_width"] ]
print(X)
print("=" * 30)