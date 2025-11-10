# 데이터프레임을 pickle로 읽기
import pandas as pd
import pickle

with open("pandas.pkl","rb") as f :
    df = pickle.load(f)
    print(df)



    