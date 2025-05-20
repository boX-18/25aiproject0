import streamlit as st
import random

# MBTI 유형에 따른 직업 추천 데이터
mbti_to_jobs = {
    'INTJ': ['과학자 🍳', '의사 🏥', '엔지니어 ⚙️', '법률 전문가 ⚖️'],
    'INTP': ['프로그램 개발자 💻', '연구원 🔬', '과학자 🧪', '작가 ✍️'],
    'ENTJ': ['기업가 💼', '경영자 🏢', '변호사 👩‍⚖️', '정치인 🗳️'],
    'ENTP': ['발명가 💡', '기술 개발자 🔧', '작가 🖋️', '경영 컨설턴트 📊'],
    'INFJ': ['심리학자 🧠', '작가 📚', '사회복지사 👫', '종교 지도자 ⛪'],
    'INFP': ['작가 ✍️', '예술가 🎨', '심리학자 🧑‍⚕️', '사회복지사 💖'],
    'ENFJ': ['교사 🍎', '인사 전문가 👥', '작가 📖', '사회복지사 🤝'],
    'ENFP': ['마케팅 전문가 📈', '작가 📝', '예술가 🎭', '창업자 🚀'],
    'ISTJ': ['회계사 📊', '변호사 ⚖️', '경찰 🚔', '군인 🎖️'],
    'ISFJ': ['간호사 💉', '교사 🏫', '사회복지사 👩‍👧', '행정직 🗂️'],
    'ESTJ': ['경영자 💼', '군인 🪖', '교사 👩‍🏫', '프로젝트 매니저 📅'],
    'ESFJ': ['간호사 💊', '선생님 👩‍🏫', '사회복지사 👩‍❤️‍👩', '영업 담당자 🛍️'],
    'ISTP': ['기계공 🔩', '과학자 🧬', '디자이너 🎨', '파일럿 ✈️'],
    'ISFP': ['예술가 🎭', '디자이너 🎨', '작곡가 🎼', '정원사 🌻'],
    'ESTP': ['사업가 💼', '운동선수 🏅', '기계공 ⚙️', '파일럿 🛩️'],
    'ESFP': ['배우 🎬', '디자이너 👗', '판매원 🛒', '엔터테이너 🎤']
}

# 랜덤 이모지 생성 함수
def random_emoji():
    emojis = ["🎉", "🎈", "🎊", "🌟", "💥", "🥳", "✨"]
    return random.choice(emojis)

# 직업 추천 및 정보 링크
def get_wikipedia_url(job):
    job_to_wiki = {
    '과학자 🍳': 'https://ko.wikipedia.org/wiki/%EA%B3%BC%ED%95%99%EC%9E%90',
    '의사 🏥': 'https://ko.wikipedia.org/wiki/%EC%9D%98%EC%82%AC',
    '엔지니어 ⚙️': 'https://ko.wikipedia.org/wiki/%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4',
    '법률 전문가 ⚖️': 'https://ko.wikipedia.org/wiki/%EB%B2%95%EB%A5%A0',
    '프로그램 개발자 💻': 'https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8_%EA%B0%9C%EB%B0%9C%EC%9E%90',
    '연구원 🔬': 'https://ko.wikipedia.org/wiki/%EC%97%B0%EA%B5%AC%EC%9B%90',
    '작가 ✍️': 'https://ko.wikipedia.org/wiki/%EC%9E%91%EA%B0%80',
    '기업가 💼': 'https://ko.wikipedia.org/wiki/%EA%B8%B0%EC%97%85%EA%B0%80',
    '경영자 🏢': 'https://ko.wikipedia.org/wiki/%EA%B2%BD%EC%98%81%EC%9E%90',
    '변호사 👩‍⚖️': 'https://ko.wikipedia.org/wiki/%EB%B3%80%ED%98%B8%EC%82%AC',
    '정치인 🗳️': 'https://ko.wikipedia.org/wiki/%EC%A0%95%EC%B9%98%EC%9D%B8',
    '마케팅 전문가 📈': 'https://ko.wikipedia.org/wiki/%EB%A7%88%EC%BC%80%ED%8C%85_%EC%A0%84%EB%AC%B8%EA%B3%BC',
    '작곡가 🎼': 'https://ko.wikipedia.org/wiki/%EC%9E%91%EC%BD%95%EA%B0%80',
    '배우 🎬': 'https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%9A%B0',
    '디자이너 🎨': 'https://ko.wikipedia.org/wiki/%EB%94%94%EC%9E%90%EC%9D%B8',
    '간호사 💉': 'https://ko.wikipedia.org/wiki/%EA%B0%84%ED%98%B8%EC%82%AC',
    '교사 🏫': 'https://ko.wikipedia.org/wiki/%EA%B5%90%EC%82%AC',
    '사회복지사 👫': 'https://ko.wikipedia.org/wiki/%EC%82%AC%ED%9A%8C%EB%B3%B5%EC%A7%80%EC%82%AC',
    '군인 🎖️': 'https://ko.wikipedia.org/wiki/%EA%B5%B0%EC%9D%B8',
    '회계사 📊': 'https://ko.wikipedia.org/wiki/%ED%9A%8C%EA%B3%84%EC%82%AC',
    '경찰 🚔': 'https://ko.wikipedia.org/wiki/%EA%B2%BD%EC%B0%B0',
    '파일럿 ✈️': 'https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC%EB%9F%9B',
    '사회복지사 👩‍❤️‍👩': 'https://ko.wikipedia.org/wiki/%EC%82%AC%ED%9A%8C%EB%B3%B5%EC%A7%80%EC%82%AC',
    '운동선수 🏅': 'https://ko.wikipedia.org/wiki/%EC%9A%B4%EB%8F%99%EC%84%A0%EC%88%98',
    '파일럿 🛩️': 'https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC%EB%9F%9B',
    '프로젝트 매니저 📅': 'https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EB%A7%A4%EB%8B%88%EC%A0%80',
    '판매원 🛒': 'https://ko.wikipedia.org/wiki/%ED%8C%90%EB%A7%A4%EC%9B%90',
    '작곡가 🎼': 'https://ko.wikipedia.org/wiki/%EC%9E%91%EC%BD%95%EA%B0%80',
    '정원사 🌻': 'https://ko.wikipedia.org/wiki/%EC%A0%95%EC%9B%90%EC%82%AC',
    '디자이너 🎨': 'https://ko.wikipedia.org/wiki/%EB%94%94%EC%9E%90%EC%9D%B8',
}

    return job_to_wiki.get(job, '#')

# 메인 화면 구성
st.title(f'MBTI 직업 추천 앱 {random_emoji()}')

st.write("""
🎈🎊 축하합니다! 🎉🎈  
당신의 MBTI에 맞는 멋진 직업을 찾았어요! 🎉🎊  
아래에서 자신의 MBTI를 선택하고, **재미있는 직업 추천**을 받아보세요! 
""")

# 사용자로부터 MBTI 입력 받기
mbti = st.selectbox('당신의 MBTI 유형을 선택하세요:', [
    'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 
    'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
])

# 추천 직업 출력
if mbti:
    st.subheader(f'{mbti}와 잘 어울리는 직업 {random_emoji()}:')
    for job in mbti_to_jobs[mbti]:
        job_url = get_wikipedia_url(job)
        st.write(f'- {job} {random_emoji()} [위키피디아]({job_url})')

# 화면 구석에 색이 바뀌는 동그라미 이모지 (실시간으로 업데이트되게)
st.markdown("""
    <style>
        @keyframes colorChange {
            0% {background-color: red;}
            25% {background-color: blue;}
            50% {background-color: green;}
            75% {background-color: yellow;}
            100% {background-color: pink;}
        }
        .circle {
            position: fixed;
            top: 10px;
            right: 10px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            animation: colorChange 4s infinite;
        }
    </style>
    <div class="circle"></div>
""", unsafe_allow_html=True)

# 풍선과 폭죽 이모지
st.write("""
🎈🎊 축하합니다! 🎉🎈  
당신의 MBTI에 맞는 멋진 직업을 찾았어요! 🎉🎊  
""")
