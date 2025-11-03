#넘파이 배열의 연산
import numpy as np

arr = np.array([1, 2, 3])
#[1, 2, 3] + [1, 1, 1]
print(arr + 1) #[2, 3, 4]
print(arr - 1) #[0, 1, 2]
print(arr * 2) #[2, 4, 6]
print(arr / 2) #[0.5, 1., 1.5]

arr = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr + arr2)
print(arr - arr2)
print(arr * arr2)
print(arr / arr2)

arr = np.array([[1,2,3], [4,5,6]])
print(arr)

print(arr + 1)
print(arr * 2)

arr2 = np.array([1,2])
#print(arr + arr2)
#브로드캐스트 연산
#차원이 낮은쪽의 값을 차원을 높여서 계산을 수행
#[1,2,3] + 1 -> [1,2,3] + [1,1,1]


#인덱싱, 슬라이싱
arr = np.array([1,2,3,4,5,6])
print(arr)
print("arr[1] : ", arr[1])
print(arr[2])
print(arr[-1])

print(arr[::])
print(arr[0:5:1])
print(arr[::-1])

arr[1:4] = [50, 60, 70]
#[2,3,4]
print(arr)







#구조분해할당
lst = [1, 2, 3, 4]
#lst변수의 요소들을 각 각 새로운 변수에 할당
a = lst[0]
b = lst[1]
c = lst[2]
d = lst[3]

a,b,c,d = lst

