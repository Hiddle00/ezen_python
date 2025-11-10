# 나이브 베이즈 감성 분석기
from sklearn.naive_bayes import MultinomialNB
# 데이터 분할 도구
from sklearn.model_selection import train_test_split
# 텍스트 벡터화 도구
from sklearn.feature_extraction.text import CountVectorizer
# 정확도 계산 도구
from sklearn.metrics import accuracy_score

import pickle

# 1. 감성 분석 데이터 준비
# 실제로 활용할때에는, 라벨링된 대량의 데이터를 준비하세요
data = [
        ('가격이 저렴하고 품질이 좋습니다.', 'pos'),
        ('배송이 빠르고 포장이 깔끔합니다.', 'pos'),
        ('디자인이 세련되고 마음에 듭니다.', 'pos'),
        ('이 제품은 정말 만족스럽습니다.', 'pos'),
        ('저 차는 성능이 매우 좋습니다.', 'pos'),
        ('서비스가 빠르고 친절합니다.', 'pos'),
        ('저 차는 성능이 매우 좋지 않습니다.', 'neg'),
        ('품질이 나쁘고 만족스럽지 않습니다.', 'neg'),
        ('배송이 느리고 포장이 부실합니다.', 'neg'),
        ('이 제품은 사용하기 불편합니다.', 'neg'),
        ('서비스가 느리고 불친절합니다.', 'neg'),
        ('디자인이 촌스럽고 별로입니다.', 'neg')
]

# 2. 문장과 라벨을 분리
sentences, labels = zip(*data)

# 3. 문장을 숫자 벡터로 변환시키는 벡터라이저 생성
vectorizer = CountVectorizer()

# 4. 문장을 벡터 형태로 변환
X = vectorizer.fit_transform(sentences)

# 5. 학습, 테스트용 데이터 분리 8:2
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# 6. 나이브 베이즈 모델 생성 및 학습
model = MultinomialNB()
model.fit(X_train, y_train)

# 7. 테스트 데이터로 모델 성능 평가
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"정확도: {accuracy * 100:.2f}%")  # 정확도 출력

# 8. 학습된 모델과, 학습데이터에 사용한 벡터라이저를 저장
with open("model.pkl",'wb') as f:
    data = (model, vectorizer)
    pickle.dump(data,f)

print("모델과 벡터라이저가 저장되었습니다")

"""
# 학습된 모델을 이용하여 예측한다.
sentence = "이 제품은 정말 만족스럽습니다"
X = vectorizer.transform([sentence])
pred = model.predict(X)
print(pred)
"""










