#DBScan 알고리즘
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rc
    
#=====================================================================
def visualize_cluster_plot(clusterobj, dataframe, label_name, iscenter=True):
    
    # 군집별 중심 위치: K-Means, Mean Shift 등
    if iscenter:
        centers = clusterobj.cluster_centers_
    
    # Cluster 값 종류
    unique_labels = np.unique(dataframe[label_name].values)
    
    markers=['o', 's', '^', 'x', '*']
    isNoise=False

    for label in unique_labels:
        # 군집별 데이터 프레임
        label_cluster = dataframe[dataframe[label_name]==label]
        
        if label == -1:
            cluster_legend = 'Noise'
            isNoise=True
        else:
            cluster_legend = 'Cluster '+str(label)
        
        # 각 군집 시각화
        plt.scatter(x=label_cluster['ftr1'], y=label_cluster['ftr2'], s=70,
                    edgecolor='k', marker=markers[label], label=cluster_legend)
        
        # 군집별 중심 위치 시각화
        if iscenter:
            center_x_y = centers[label]
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=250, color='white',
                        alpha=0.9, edgecolor='k', marker=markers[label])
            plt.scatter(x=center_x_y[0], y=center_x_y[1], s=70, color='k',\
                        edgecolor='k', marker='$%d$' % label)
            
    if isNoise:
        legend_loc='upper center'
    else: 
        legend_loc='upper right'
    
    plt.legend(loc=legend_loc)
    plt.show()
#=====================================================================

iris_pd = pd.read_csv("iris_encode.csv")
print(iris_pd.head())
print("=" * 30)


features = iris_pd[ ['petal_length', 'petal_width', 'sepal_length', 'sepal_width'] ]
labels = list(iris_pd['species'])

from sklearn.cluster import DBSCAN

#dbscan = DBSCAN(eps=0.6, min_samples=8, metric='euclidean')
dbscan = DBSCAN(eps=0.9, min_samples=8, metric='euclidean')
dbscan_labels = dbscan.fit_predict(features)

#군집 레이블이 -1인 것은 노이즈에 속하는 군집을 의미
print(labels)
print(list(dbscan_labels))
print("=" * 30)

from sklearn.decomposition import PCA

# pca로 피처 2개만 사용
pca = PCA(n_components=2, random_state=0)
pca_transformed = pca.fit_transform(features)
print(pca_transformed)
print("=" * 30)


# 데이터 프레임에 주성분 추가
iris_pd["ftr1"] = pca_transformed[:,0]
iris_pd["ftr2"] = pca_transformed[:,1]

iris_pd['dbscan_cluster'] = dbscan_labels
iris_pd['target'] = labels

iris_result = iris_pd.groupby(['target'])['dbscan_cluster'].value_counts()
print(iris_result)

visualize_cluster_plot(dbscan, iris_pd, "dbscan_cluster", iscenter=False)









