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


# 직업과 하위 직업들에 대한 정보
job_to_subjobs = {
    '과학자 🍳': {
        'description': '과학자는 새로운 발견을 위해 실험과 연구를 수행하는 전문가입니다.',
        'subjobs': [
            '물리학자 🔬: 자연의 법칙을 연구하는 과학자',
            '화학자 🧪: 화학 반응과 물질을 연구하는 과학자',
            '생물학자 🧬: 생명과학에 대한 연구를 수행하는 과학자',
            '천문학자 🌌: 우주와 천체를 연구하는 과학자'
        ]
    },
    '의사 🏥': {
        'description': '의사는 사람들의 건강을 돌보는 전문가입니다.',
        'subjobs': [
            '심장 전문의 ❤️: 심장 관련 질환을 진단하고 치료하는 의사',
            '내과 의사 🩺: 다양한 내과 질환을 치료하는 의사',
            '외과 의사 ⚒️: 수술을 통해 질환을 치료하는 의사',
            '소아과 의사 👶: 어린이의 건강을 돌보는 의사'
        ]
    },
    '엔지니어 ⚙️': {
        'description': '엔지니어는 다양한 기술적 문제를 해결하는 전문가입니다.',
        'subjobs': [
            '기계 엔지니어 🔧: 기계 설계 및 제조와 관련된 문제를 해결하는 엔지니어',
            '전기 엔지니어 ⚡: 전기 시스템 설계와 설치를 담당하는 엔지니어',
            '소프트웨어 엔지니어 💻: 컴퓨터 프로그램을 설계하고 개발하는 엔지니어',
            '토목 엔지니어 🏗️: 구조물 및 인프라 설계를 담당하는 엔지니어'
        ]
    },
    '변호사 👩‍⚖️': {
        'description': '변호사는 법적 문제를 해결하고, 법원에서 클라이언트를 대리하는 전문가입니다.',
        'subjobs': [
            '형사 변호사 ⚖️: 형사 사건을 전문적으로 다루는 변호사',
            '민사 변호사 📜: 민사 소송과 관련된 법적 절차를 처리하는 변호사',
            '기업 변호사 💼: 기업과 관련된 법적 문제를 다루는 변호사',
            '가족 변호사 👨‍👩‍👧‍👦: 가족 관련 법적 문제를 전문적으로 다루는 변호사'
        ]
    },
    '프로그램 개발자 💻': {
        'description': '프로그램 개발자는 컴퓨터 프로그램을 설계하고 개발하는 전문가입니다.',
        'subjobs': [
            '프론트엔드 개발자 🌐: 웹 페이지의 사용자 인터페이스를 설계하는 개발자',
            '백엔드 개발자 🖥️: 서버와 데이터베이스 관련 프로그램을 개발하는 개발자',
            '풀스택 개발자 ⚙️: 프론트엔드와 백엔드를 모두 다루는 개발자',
            '모바일 앱 개발자 📱: 스마트폰 및 태블릿용 앱을 개발하는 개발자'
        ]
    },
    '디자이너 🎨': {
        'description': '디자이너는 시각적이고 기능적인 디자인을 창조하는 전문가입니다.',
        'subjobs': [
            '그래픽 디자이너 🖌️: 시각적 콘텐츠를 디자인하는 전문가',
            'UX/UI 디자이너 🎮: 사용자 경험과 인터페이스를 설계하는 디자이너',
            '산업 디자이너 🏭: 제품의 외형과 기능을 설계하는 디자이너',
            '패션 디자이너 👗: 의류와 액세서리 디자인을 전문으로 하는 디자이너'
        ]
    }
}

# 랜덤 이모지 생성 함수
def random_emoji():
    emojis = ['🎉', '✨', '💫', '🎈', '🎊']
    return random.choice(emojis)

# Streamlit 앱 설정
st.title("당신에게 맞는 직업과 하위 직업을 알아보세요! {random_emoji()}")

# MBTI 입력 받기
mbti = st.selectbox("당신의 MBTI를 선택하세요:", ['INTJ', 'ENTP', 'ISFJ', 'ESTP', 'INFJ', 'ENFP', 'ISTJ', 'ESFP'])

# 직업 추천 및 하위 직업 출력
if mbti == 'INTJ':
    job = '과학자 🍳'
elif mbti == 'ENTP':
    job = '변호사 👩‍⚖️'
elif mbti == 'ISFJ':
    job = '교사 🏫'
elif mbti == 'ESTP':
    job = '경찰 🚔'
elif mbti == 'INFJ':
    job = '작가 ✍️'
elif mbti == 'ENFP':
    job = '디자이너 🎨'
elif mbti == 'ISTJ':
    job = '엔지니어 ⚙️'
elif mbti == 'ESFP':
    job = '배우 🎬'

# 직업과 하위 직업 정보 출력
st.subheader("{job}에 대해 알아보세요! {random_emoji()}")
st.write(job_to_subjobs[job]['description'])

# 하위 직업 리스트
st.subheader("하위 직업들:")
for subjob in job_to_subjobs[job]['subjobs']:
    st.write("- {subjob}")

# 추가적으로 직업에 대한 링크 제공
st.markdown("[자세한 직업 정보 읽기](https://ko.wikipedia.org/wiki/{job_to_wiki[job]})")

# 화면 구석에 색이 바뀌는 동그라미 이모지 표시
st.markdown(
    """
    <style>
    .circle {
        position: fixed;
        top: 50%;
        left: 50%;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: #ff69b4;
        animation: colorChange 3s infinite;
    }
    @keyframes colorChange {
        0% { background-color: #ff69b4; }
        50% { background-color: #32cd32; }
        100% { background-color: #ff69b4; }
    }
    </style>
    <div class="circle"></div>
    """,
    unsafe_allow_html=True
)

