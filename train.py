from gensim.models import FastText
import pandas as pd

# 데이터 전처리
with open('tokenized_data.txt', 'r') as file:
    projects = [line.strip().split() for line in file]


# Word2Vec 모델 학습
model = FastText(sentences=projects, min_count=1, sg=1, negative=5, epochs=10, hs=0, vector_size=100, window=9999999, workers=4)

model.save('project_model')

# def recommend_project(input_keywords):
#     # 모든 프로젝트에 대한 유사도 점수를 저장할 딕셔너리
#     project_scores = {}

#     # 모든 프로젝트를 순회
#     for i, project in enumerate(projects):
#         # 프로젝트의 키워드와 입력 키워드 간의 유사도를 저장할 리스트
#         similarities = []

#         # 프로젝트의 모든 키워드를 순회
#         for keyword in project:
#             # 키워드가 모델의 단어 벡터에 존재하는 경우에만 유사도를 계산
#             for input_keyword in input_keywords:
#                 if keyword in model.wv and input_keyword in model.wv:
#                     similarity = model.wv.similarity(keyword, input_keyword)
#                     similarities.append(similarity)

#         # 프로젝트의 유사도 점수는 키워드 간 유사도의 평균
#         if similarities:
#             project_scores[i] = sum(similarities) / len(similarities)

#     # 가장 높은 점수를 가진 프로젝트를 찾음
#     most_similar_project_index = max(project_scores, key=project_scores.get)

#     return projects[most_similar_project_index]

# def calculate_similarity_scores(tech_stack):
#     # 모든 프로젝트에 대한 유사도 점수를 저장할 딕셔너리
#     project_scores = {}

#     # 모든 프로젝트를 순회
#     for project in projects:
#         # 프로젝트의 기술 스택과 주어진 기술 스택 간의 유사도를 저장할 리스트
#         similarities = []

#         # 프로젝트의 모든 기술 스택을 순회
#         for tech in project:
#             # 기술 스택이 모델의 단어 벡터에 존재하는 경우에만 유사도를 계산
#             if tech in model.wv and tech_stack[0] in model.wv:
#                 similarity = model.wv.similarity(tech, tech_stack[0])
#                 similarities.append(similarity)

#         # 프로젝트의 유사도 점수를 계산 (유사도의 평균)
#         if similarities:
#             project_scores[str(project)] = sum(similarities) / len(similarities)

#     return project_scores

# def get_most_similar_project(tech_stack):
#     # 각 프로젝트의 유사도 점수를 계산
#     project_scores = calculate_similarity_scores(tech_stack)

#     # 가장 높은 점수를 가진 프로젝트를 찾음
#     most_similar_project = max(project_scores, key=project_scores.get)

#     return most_similar_project

# # 예시
# print(calculate_similarity_scores(['건강', '앱', '개발', '기획']))
# # 예시
# print(get_most_similar_project(['소프트', '모바일', '텔레콤', 'Phone', '쇼핑몰']))

# print(recommend_project(['건강', '앱']))