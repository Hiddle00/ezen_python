# 학습된 나이브 베이즈 감성 분석기 모델을 로드한다.
import pickle

# 1. 저장된 모델과 벡터라이저 불러오기
with open("model.pkl","rb") as f :
    model, vectorizer = pickle.load(f)
    
# 2. 감성 분류를 수행한다.
sentence = "이 제품은 정말 만족스럽습니다"
X = vectorizer.transform([sentence])
pred = model.predict(X)
print(pred)

# 3. 감성 분석 추론과 확률 계산
per = model.predict_proba(X)[0]
print(f"부정 점수 : {per[0] * 100:.2f}%")
print(f"긍정 점수 : {per[1] * 100:.2f}%")

