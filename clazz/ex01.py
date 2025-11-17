# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:11:13 2025

@author: MYCOM
"""

class Car :
    def __init__(self, a) :
        print("Car 클래스 호출!", a)
        
    def drive(self, name) :
        print("차가 달립니다.")
#기본생성자O
#java의 this = self
#파라미터가 추가로 필요하면 self뒤에
#함수는 파라미터가 정의되어있는데 들어오지 않으면 None
#생성자는 오류발생

#Python class의 생성자는 def __init__(self) : 으로 선언한다.
#Python class의 생성자와 함수는 반드시 첫번째 파라미터로 self를 받아야한다.

car = Car("아우디")

print(car)

car.drive(2) #True, 2.0 : O  / 없으면 오류

