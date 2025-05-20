import streamlit as st
import random
import requests
from PIL import Image
from io import BytesIO

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

# 윈도우 풍경 이미지 URL 리스트 (인터넷에서 사용 가능한 이미지 URL)
background_images_urls = [
    "https://images.unsplash.com/photo-1506748686211-0d38b4202823",  # 예시: Windows-like background
    "https://images.unsplash.com/photo-1506748686211-0d38b4202823",  # 예시 이미지 링크 (윈도우 배경 풍경 느낌)
    "https://images.unsplash.com/photo-1472053238851-d01f4fe8db34",  # 예시: 또 다른 배경
]

# 랜덤 이미지 선택
def get_random_background_image():
    return random.choice(background_images_urls)

# 배경 이미지 로딩
background_image_url = get_random_background_image()
response = requests.get(background_image_url)
img = Image.open(BytesIO(response.content))

# 메인 화면 구성
st.title(f'MBTI 직업 추천 앱 {random_emoji()}')

st.image(img, use_column_width=True, caption="윈도우 풍경 배경")

st.write("""
이 앱은 **MBTI** 유형을 입력하면, 그에 맞는 직업을 추천해줍니다!  
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
        st.write(f'- {job} {random_emoji()}')

# 풍선과 폭죽 이모지
st.write("""
🎈🎊 축하합니다! 🎉🎈  
당신의 MBTI에 맞는 멋진 직업을 찾았어요! 🎉🎊  
""")

# 실행 방법 안내
st.write("""
즐거운 직업 추천을 받아보세요! 🎈🎉
""")


