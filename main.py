import streamlit as st
import random
import time

# MBTI별 직업 추천 데이터 (이모지 추가)
mbti_jobs = {
    "INTJ": ("전략 컨설턴트, 데이터 분석가, 연구원", "🧑‍💼"),
    "INTP": ("소프트웨어 개발자, 데이터 과학자, 발명가", "💻"),
    "ENTJ": ("CEO, 기업 전략가, 사업 개발 관리자", "👩‍💼"),
    "ENTP": ("창업자, 광고 전략가, 변호사", "🧑‍⚖️"),
    "INFJ": ("심리학자, 사회 사업가, 교사", "🧑‍🏫"),
    "INFP": ("작가, 예술가, 상담사", "✍️"),
    "ENFJ": ("팀 리더, 교육자, 마케팅 전문가", "👩‍🏫"),
    "ENFP": ("작가, 배우, 인간 관계 전문가", "🎭"),
    "ISTJ": ("법률 전문가, 경영 컨설턴트, 회계사", "👨‍⚖️"),
    "ISFJ": ("간호사, 사회 복지사, 교육자", "👩‍⚕️"),
    "ESTJ": ("관리자, 법률 사무직, 프로젝트 관리자", "📋"),
    "ESFJ": ("교사, 건강 관리 전문가, 마케팅 전문가", "🧑‍🏫"),
    "ISTP": ("기술자, 조종사, 엔지니어", "🛠️"),
    "ISFP": ("디자이너, 예술가, 사진작가", "🎨"),
    "ESTP": ("기업가, 마케팅 전문가, 이벤트 플래너", "📈"),
    "ESFP": ("연예인, 이벤트 기획자, 사회 활동가", "🎤")
}

# 네온 색상 리스트
neon_colors = [
    "#FF073A", "#FF3399", "#FF66FF", "#FF00FF", "#FF6666", "#FF33CC", "#FF00CC", 
    "#FF0066", "#FF6600", "#FF9900", "#FFCC00", "#FFCC66", "#FF6666", "#00FF00",
    "#00FF66", "#00FF99", "#00FFFF", "#0099FF", "#0066FF", "#0000FF", "#6600FF",
    "#9900FF", "#CC00FF", "#FF00FF", "#FF3399"
]

# 스트림릿 UI 설정
st.title("🎉 MBTI 직업 추천 웹앱 🎉")

# MBTI 입력 받기
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", 
                                                "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", 
                                                "ISTP", "ISFP", "ESTP", "ESFP"])

# 직업 추천
if mbti in mbti_jobs:
    job, emoji = mbti_jobs[mbti]
    st.subheader(f"추천 직업 for {mbti}: {emoji}")
    st.write(job)

# 네온 색상 변경 함수 (계속해서 색이 바뀌도록)
def change_color():
    while True:
        # 랜덤 색상 선택
        bg_color = random.choice(neon_colors)
        text_color = random.choice(neon_colors)

        # 배경색과 글자색 변경
        st.markdown(
            f"<style>body {{background-color: {bg_color}; color: {text_color};}}</style>", 
            unsafe_allow_html=True
        )
        
        time.sleep(0.5)  # 0.5초마다 색상 변경

# 색상 변경 시작
if __name__ == "__main__":
    change_color()  # 계속해서 색상 변경
