# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:47:56 2025

@author: MYCOM
"""
#Python class의 getter/setter

class Person() :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def set_name(self, name) :
        self.name = name

    def get_name(self) :
        return self.name
    
    #데코레이터
    #객체나 함수를 직접 수정하지 않고 추가적인 기능을 덧붙이는 방법
    @property  #getter메서드
    def age(self) : 
        return self.age
    
    @age.setter() #setter @age
    def age(self, age) :
        self.age = age
        
p = Person("홍길동", 25)
name = p.get_name()
print(name)

p.set_name("전우치")
name = p.get_name()
print(name)

#필드에 __를 붙이면 적어도 직접 접근은 못한다

p.age = 30
age = p.age
print(age)