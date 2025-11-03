#numpy
#numpy는 고성능 다차원 배열을 지원하는
#파이썬 라이브러리

import numpy as np

lst = [1, 2, 3]
print(type(lst))
print(lst)

#넘파이 배열 생성
array = np.array(lst)
print(type(array))
print(array)

#리스트의 연산
print(lst)

#넘파이의 연산
print(array + 2)


#넘파이 배열 직접 생성
zero_array = np.zeros((1, 3))
print(zero_array)
#1행 3열 2차원배열을 생성하고
#모든 요소를 0.0으로 채운다.

ones_array = np.ones((2, 4))
print(ones_array)
print(ones_array.shape)
#2행 4열 2차원배열을 생성하고
#모든 요소를 1.0으로 채운다.

full_array = np.full((5, 2), 5)
print(full_array)
print(full_array.shape)
#5행 2열 2차원배열을 생성하고
#모든 요소를 5로 채운다

#넘파이 배열의 속성
arr = np.array([1,2,3])
print(arr)
print(arr.shape) 
#배열의 형태(3,) / 1차원배열, 3개의 요소

print(arr.ndim)
#배열의 차원수 / 1

print(arr.size)
#배열의 전체 요소 개수 / 3

print(arr.dtype)
#배열 요소의 데이터 타입


arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

print(arr2.shape)   #2행 3열
print(arr2.ndim)    #2차원
print(arr2.size)    #6개
print(arr2.dtype)   #int

#넘파이 배열을 생성 할 때 데이터타입 변경
data = np.zeros((4, 5), dtype=np.int32)
print(data)