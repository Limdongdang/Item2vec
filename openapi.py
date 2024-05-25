import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
access_key = os.getenv("ACCESS_KEY")

# API 요청
url = f"https://oapi.saramin.co.kr/job-search?access-key={access_key}&ind_cd=3&count=110"
response = requests.get(url)

# JSON 파싱
data = response.json()

# 각 job에서 필요한 정보 추출
projects = []
for job in data['jobs']['job']:
    project = []
    project.append(job['position']['title'])  # job title
    project.append(job['position']['location']['name'])  # job location
    project.append(job['position']['experience-level']['name'])  # job experience
    project.append(job['position']['required-education-level']['name'])  # job education
    project.append(job['keyword'])  # job keyword
    projects.append(project)

# DataFrame 생성
df = pd.DataFrame(projects, columns=['Title', 'Location','Experience-Level', 'requried-education-level', 'Keyword'])

# 엑셀 파일로 저장
df.to_excel('projects.xlsx', index=False)