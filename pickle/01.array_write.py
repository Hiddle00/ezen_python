# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 16:03:59 2025

@author: MYCOM
"""
#pickle은 python에서 자료를 파일로 저장하고 읽는 모듈
import pickle

data = [1, 2, 3, 4]

# 파일에 데이터를 저장하기
with open("list.pkl", "wb") as f :
    pickle.dump(data,f)
print("LIST 데이터를 저장했습니다.")

data = {"홍길동" : 170, "성춘향" : 150}
with open("dict.pkl", "wb") as f :
    pickle.dump(data,f)
print("파일에 dictionary 데이터를 저장했습니다.")