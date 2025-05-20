import streamlit as st
import random

# 직업 추천 리스트 (MBTI 타입에 따라 직업 추천)
job_recommendations = {
    'INTJ': [("과학자 🧑‍🔬", "https://www.bls.gov/ooh/life-physical-and-social-science/")],
    'INTP': [("연구원 🔬", "https://www.bls.gov/ooh/life-physical-and-social-science/")],
    'ENTJ': [("경영자 👔", "https://www.bls.gov/ooh/management/")],
    'ENTP': [("발명가 💡", "https://www.bls.gov/ooh/architecture-and-engineering/")],
    'INFJ': [("심리학자 🧠", "https://www.bls.gov/ooh/life-physical-and-social-science/")],
    'INFP': [("작가 ✍️", "https://www.bls.gov/ooh/media-and-communication/writers-and-authors.htm")],
    'ENFJ': [("교사 🍎", "https://www.bls.gov/ooh/education-training-and-library/high-school-teachers.htm")],
    'ENFP': [("사회 활동가 🌍", "https://www.bls.gov/ooh/community-and-social-service/social-and-human-service-assistants.htm")],
    'ISTJ': [("회계사 💼", "https://www.bls.gov/ooh/business-and-financial/accountants-and-auditors.htm")],
    'ISFJ': [("간호사 🩺", "https://www.bls.gov/ooh/healthcare/registered-nurses.htm")],
    'ESTJ': [("경영 관리자 🏢", "https://www.bls.gov/ooh/management/")],
    'ESFJ': [("사회 복지사 💖", "https://www.bls.gov/ooh/community-and-social-service/social-workers.htm")],
    'ISTP': [("기계공 🛠️", "https://www.bls.gov/ooh/installation-maintenance-and-repair/diesel-mechanics.htm")],
    'ISFP': [("디자이너 🎨", "https://www.bls.gov/ooh/arts-and-design/fashion-designers.htm")],
    'ESTP': [("세일즈 전문가 💼", "https://www.bls.gov/ooh/sales/sales-managers.htm")],
    'ESFP': [("연예인 🎤", "https://www.bls.gov/ooh/entertainment-and-sports/actors.htm")],
}

# 랜덤 이모지 생성 함수
def get_random_emoji():
    emojis = ['🎉', '🎈', '🌟', '🌈', '💫']
    return random.choice(emojis)

# 메인 화면 설정
st.title(f"{get_random_emoji()} MBTI 직업 추천 웹앱 {get_random_emoji()}")

# MBTI 입력 받기
mbti = st.selectbox("당신의 MBTI 유형을 선택하세요", list(job_recommendations.keys()))

# 추천 직업 보여주기
st.subheader(f"{mbti}에 어울리는 직업은...?")

if mbti in job_recommendations:
    for job, link in job_recommendations[mbti]:
        st.write(f"- {job} [자세히 보기]({link})")

# 메인 화면에 풍선과 폭죽 이모지 추가
st.markdown("🎉🎈🎉🎈🎉 폭죽과 풍선이 당신을 기다립니다! 🎉🎈🎉🎈🎉")

