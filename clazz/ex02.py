# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 09:26:19 2025

@author: MYCOM
"""

class Animal : 
    def __init__(self) :
        #파이썬 클래스의 필드는 생성자 안에서 self.필드이름 = 초기값으로 선언.
        self.name = None
        self.age = None
    def sound(self) :
        #함수 내부에서도 필드를 선언할 수 있다.
        self.sound = None
        self.sounds = None
#필드를 선언만 해두는것은 불가능. 뭐라도 하나 넣어줘야
#함수 안에서도 필드선언이 가능하지만 하지말것
#동적으로 만들기 때문에 나중에 메서드를 호출 했을때 헷갈림
a = Animal()
print(a.name)
print(a.age)
print(a.sound)      #함수 주소
#필드와 함수 이름이 겹치면 찾을방도가 없다
a.sound()
print(a.sounds)

#접근제한자
#self.name -> puplic name
#self._name -> protected name
#self.__name -> private name
#외부에서 접근하지 못하도록 변수이름을 바꿔버린다 ㅋㅋㅋ
#존재는 하지만 거의 사용하지 않음
#__name으로 선언하면 클래스 내부에서도 __name으로 접근해야 한다.
class Person() : 
    def __init__(self, name=None, age=0) :
        self.name = name
        self.age = age
    def prints(self) :
        #print(f"이름은 : {name}") 오류
        print(f"이름은 : {self._name}")
        print(f"나이는 : {self._age}")

# 타입이 명확하지 않기 때문에 무엇을 찾아가야 할지 애매하다
# = 오버로딩 x

p = Person("홍길동", 25)
p.prints()

#파라미터에 기본값을 넣어두면 오버로딩과 비슷하게 사용가능
p = Person()
p.prints()
#print(p.__name)
#__name -> _Person__name -> _클래스이름__필드이름