#넘파이 배열의  통계
#합계, 평균, 최솟값...
import numpy as np

data = [25, 37, 12, 18, 59, 60, 93]
arr = np.array(data)

print(arr)
#합계
print(arr.sum())
print(np.sum(arr))

#평균
print(arr.mean())

#분산
print(arr.var())

#표준편차
print(arr.std())
#print(arr.)

#넘파이 배열의 축
arr = np.array([[1,2,3],[4,5,6]])

"""
     [
       [1,2,3],
       [4,5,6]
     ]
"""

print(np.sum(arr)) #모든 요소의 합계

print(np.sum(arr, axis=0))
# [1, 2, 3]
#+[4, 5, 6]
# [(1 + 4), (2 + 5), (3 + 6)]
#[[5,7,9]]
#axis 0 -> 행

print(np.sum(arr,axis=1))
# [1, + 2, + 3]
# [4, + 5, + 6]
#[6,15]
#axis 1 -> 열

#넘파이 배열에서 축 변경
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

#역행렬, 행과 열의 축을 바꾼다
#(2, 3) -> (3, 2) shape
print(arr.T)

#넘파이 배열에서 차원 변경
print(arr.shape)
#(2, 3)

print(arr.reshape(3, 2))
#(2, 3) -> (3, 2)
print(arr.reshape(6, 1))
#(2, 3) -> (6, 1)
print(arr.reshape(1, 6))
#(2, 3) -> (1, 6)
print(arr.reshape(6))
#(2, 3) -> (6,)