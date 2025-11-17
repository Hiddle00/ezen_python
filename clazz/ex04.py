# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:59:32 2025

@author: MYCOM
"""
#상속
class Animal :
    def __init__(self) :
        print("Animal 클래스 생성")
    def sound(self) :
        print("동물이 소리를 냅니다.")

#Dog클래스에서 Animal클래스를 상속    
class Dog(Animal) :  #java의 extends
    def __init__(self) :
        super().__init__()
        print("dog 생성")
        
    def bark(self) :
        print("멍멍")
        
    #자식클래스가 sound함수를 오버라이딩
    def sound(self) :
        super().sound() #super()생성자를 이용해 부모 객체에 접근
        print("강아지가 소리를 냅니다.") #그냥 덮어씌우는 듯?
        super

d = Dog()
d.bark()
d.sound()

#다중상속, static