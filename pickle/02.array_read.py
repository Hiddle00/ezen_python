# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 16:04:19 2025

@author: MYCOM
"""
#pickle은 python에서 자료를 파일로 저장하고 읽는 모듈
import pickle

# 파일에 데이터를 읽어오기
with open("list.pkl", "rb") as f : # read binury
    data = pickle.load(f)
    print(data)
    
# 파일에 데이터를 읽어오기
with open("dict.pkl", "rb") as f : 
    data = pickle.load(f)
    print(data)