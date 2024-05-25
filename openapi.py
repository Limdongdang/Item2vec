import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
access_key = os.getenv("ACCESS_KEY")

# API 요청
failc = 0 # 실패 항목
pageCount = 100  # 페이지 수
projects = []

for count in range(0, pageCount):
    try:
        url = f"https://oapi.saramin.co.kr/job-search?access-key={access_key}&job_mid_cd=2&count=110&start={count}"
        response = requests.get(url)
        # JSON 파싱
        data = response.json()
        # 각 job에서 필요한 정보 추출
        for job in data['jobs']['job']:
            project = []
            project.append(job['position']['title'])  # job title
            project.append(job['position']['industry']['name'])  # job industry
            project.append(job['position']['job-code']['name'])  # job industry
            project.append(job['position']['required-education-level']['name'])  # job education
            project.append(job['keyword'])  # job keyword
            projects.append(project)
        count += 1
    except:
        failc += 1

print(str(count)+"개 중 "+str(failc)+"개 실패 "+str(count-failc)+"개 파싱 완료")


# DataFrame 생성
df = pd.DataFrame(projects, columns=['Title', 'Industry','Job-code','requried-education-level', 'Keyword'])

# 엑셀 파일로 저장
df.to_excel('projects.xlsx', index=False)