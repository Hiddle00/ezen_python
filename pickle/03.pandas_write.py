# 데이터프레임을 pickle로 저장
import pandas as pd

# 딕셔너리를 이용하여 데이터프레임 생성
dict_data = {
    "이름" : [ "홍길동", "김길동", "박길동"],
    "수학" : [ 11, 21, 31 ],
    "영어" : [ 12, 22, 32 ],
    "국어" : [ 13, 23, 33 ]
    }

df = pd.DataFrame(dict_data)
print(df)
print("=" * 40)

import pickle
with open("pandas.pkl","wb") as f :
    pickle.dump(df,f)

print("데이터 프레임을 저장하였습니다.")    


