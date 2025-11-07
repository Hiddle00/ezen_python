# K-Means 알고리즘
import warnings
warnings.filterwarnings("ignore")

import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

#k-means 알고리즘 설명용 이미지 출력
mglearn.plots.plot_kmeans_algorithm()
plt.show()

#=====================================
#필기체 이미지 데이터를 로딩한다.
#digits는 아래와 같이 dictionary 형태의 데이터로 구성
#dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])
#data : 필기체 이미지 (1797 개)
#target : 필기체 이미지에 대한 숫자 정답
#images : 필기체 이미지에 대한 히트맵
digits = load_digits()
print(digits.keys())
print(len(digits["data"]))

#필기체 이미지 히트맵 출력
fig, axes = plt.subplots(2, 5, figsize=(10, 5),
                         subplot_kw={'xticks':(), 
                                     'yticks': ()})

for ax, img in zip(axes.ravel(), digits.images):
    ax.imshow(img)

#=====================================
# PCA 모델을 생성합니다
# n_components : 주성분 갯수
pca = PCA(n_components=1)
pca.fit(digits.data)

print(digits.data[0])
print("=" * 30)


#=====================================  
#주성분을 챠트로 표시
from matplotlib import rc
#한글폰트 설정
rc("font",family="gulim")

# 처음 두 개의 주성분으로 숫자 데이터를 변환합니다
digits_pca = pca.transform(digits.data)
print(digits_pca)
print("=" * 30)

colors = ["#476A2A", "#7851B8", "#BD3430", "#4A2D4E", "#875525",
          "#A83683", "#4E655E", "#853541", "#3A3120","#535D8E"]
plt.figure(figsize=(10, 10))
plt.xlim(digits_pca[:, 0].min(), digits_pca[:, 0].max())
plt.ylim(digits_pca[:, 1].min(), digits_pca[:, 1].max())
for i in range(len(digits.data)):
    # 숫자 텍스트를 이용해 산점도를 그립니다
    plt.text(digits_pca[i, 0], digits_pca[i, 1], str(digits.target[i]),
             color = colors[digits.target[i]],
             fontdict={'weight': 'bold', 'size': 9})
plt.xlabel("첫 번째 주성분")
plt.ylabel("두 번째 주성분")
plt.show()

#=====================================  
#k-means 알고리즘으로 비지도 학습 처리 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale


#데이터를 스케일링한다.
print(digits.data[0])
data = scale(digits.data)
print(data[0])
print("=" * 30)

#k-means 학습
#algorithm : lloyd, elkan
km = KMeans(n_clusters=10,algorithm="elkan")
km.fit(data)

#학습데이터를 이용하여 필기체 숫자를 
#분류해 본다.
predict_y = km.predict(data)

for n in range(0,3) :
    print("정답숫자 :" , digits.target[n])
    print("예측숫자:", predict_y[n])
    print("=" * 30)
    
    











