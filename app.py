from gensim.models import FastText
from utils.jamo import word_to_jamo
import pandas as pd

df = pd.read_excel('projects.xlsx')
firstvalue = ' '.join(df.values[184].astype(str))
secondvalue = ' '.join(df.values[4].astype(str))
print('1번 값: ', firstvalue)
print('2번 값: ', secondvalue)
# 모델 불러오기
loaded_model = FastText.load("models/project_model")

# print 

# 유사도 계산
similarity = loaded_model.wv.similarity(word_to_jamo(firstvalue), word_to_jamo(secondvalue))

print('1번과 2번 비교 값', similarity)

from heapq import nlargest

# 입력 값
input_value = ' '.join(df.values[184].astype(str))

# 유사도 결과를 저장할 딕셔너리
similarity_results = {}

# df.values 값 7590개와 입력 값 비교
for i in range(7590):
    comparison_value = ' '.join(df.values[i].astype(str))
    if comparison_value != input_value:
        similarity = loaded_model.wv.similarity(word_to_jamo(input_value), word_to_jamo(comparison_value))
        similarity_results[comparison_value] = similarity

# 유사도에 따라 상위 5개 결과 출력
print('1번의 유사한 상위 5개')
top_5 = nlargest(5, similarity_results, key=similarity_results.get)
for value in top_5:
    print(f"Value: {value}, Similarity: {similarity_results[value]}")