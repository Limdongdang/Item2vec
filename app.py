from gensim.models import Word2Vec
import pandas as pd

# 데이터 전처리
# projects는 프로젝트의 리스트이며, 각 프로젝트는 기술 스택의 리스트입니다.
# 예: projects = [['python', 'django', 'postgresql'], ['java', 'spring', 'mysql'], ...]
df = pd.read_excel('projects.xlsx')
projects = df['Keyword'].str.split(',')

# Word2Vec 모델 학습
model = Word2Vec(projects, min_count=1, sg=1, negative=5)

def calculate_similarity_scores(tech_stack):
    # 모든 프로젝트에 대한 유사도 점수를 저장할 딕셔너리
    project_scores = {}

    # 모든 프로젝트를 순회
    for project in projects:
        # 프로젝트의 기술 스택과 주어진 기술 스택 간의 유사도를 저장할 리스트
        similarities = []

        # 프로젝트의 모든 기술 스택을 순회
        for tech in project:
            # 기술 스택이 모델의 단어 벡터에 존재하는 경우에만 유사도를 계산
            if tech in model.wv and tech_stack[0] in model.wv:
                similarity = model.wv.similarity(tech, tech_stack[0])
                similarities.append(similarity)

        # 프로젝트의 유사도 점수를 계산 (유사도의 평균)
        if similarities:
            project_scores[str(project)] = sum(similarities) / len(similarities)

    return project_scores

def get_most_similar_project(tech_stack):
    # 각 프로젝트의 유사도 점수를 계산
    project_scores = calculate_similarity_scores(tech_stack)

    # 가장 높은 점수를 가진 프로젝트를 찾음
    most_similar_project = max(project_scores, key=project_scores.get)

    return most_similar_project

# 예시
print(calculate_similarity_scores(['Phone']))
# 예시
print(get_most_similar_project(['Phone']))