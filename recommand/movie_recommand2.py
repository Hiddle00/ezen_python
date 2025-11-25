import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time

# 1. 파일 불러오기
df = pd.read_csv('movie_list_cleaned.csv')
total_movies = len(df)

df = df.fillna("")
df["title"] = df["title"].str.strip()

# 2. 벡터화 (7만 개 전체 변환)
print("텍스트 분석(벡터화) 중...")
tfidf = TfidfVectorizer(min_df=1, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(df['features'])
print(f"-> 벡터 행렬 크기: {tfidf_matrix.shape}")

# -----------------------------------------------------------
# 타겟 설정
# -----------------------------------------------------------
target_title = "컨저링 하우스"
target_idx = df[df['title'] == target_title].index[0]

print(f"-> '{target_title}'와 나머지 {total_movies}개 영화 비교 시작...")

# -----------------------------------------------------------
# 배치 처리 (메모리 절약 + 전체 스캔)
# -----------------------------------------------------------
batch_size = 500  # 한 번에 5000개씩 비교
all_sim_scores = []

start_time = time.time()

# 0부터 70000까지 5000단위로 점프하며 전체 스캔
for i in range(0, total_movies, batch_size):
    # 어디까지 검사할지 결정
    end = min(i + batch_size, total_movies)
    
    # 1. 타겟 영화 벡터 (1개)
    target_vec = tfidf_matrix[target_idx]
    
    # 2. 비교할 영화들 벡터 (5000개)
    batch_vec = tfidf_matrix[i:end]
    
    # 3. 계산
    sim = cosine_similarity(target_vec, batch_vec)
    
    # 4. 결과 저장 (1차원으로 펴서)
    all_sim_scores.extend(sim.flatten())
    
    print(f"진행률: {end}/{total_movies} 완료")

print(f"-> 계산 종료. 소요 시간: {time.time() - start_time:.2f}초")

# -----------------------------------------------------------
# 정렬 및 출력
# -----------------------------------------------------------
# 리스트를 시리즈로 변환
scores_series = pd.Series(all_sim_scores)

# 정렬 (판다스 기능)
sorted_scores = scores_series.sort_values(ascending=False)

# 상위 3개 (본인 제외)
top_indices = sorted_scores.index[1:4]
top_values = sorted_scores.iloc[1:4]

# 결과 데이터프레임 생성
results = df.iloc[top_indices].copy()
results['similarity'] = top_values.values

print("\n--- 최종 추천 결과 ---")
print(results[['title', 'similarity', 'genre', 'plot']])