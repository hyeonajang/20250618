import streamlit as st

# 🔁 openai 설치 여부 확인
try:
    import openai
except ImportError:
    st.error("❗ 'openai' 모듈이 설치되지 않았습니다. 아래 명령어로 설치해주세요:\n\n`pip install openai`")
    st.stop()

import os

# 🌐 API 키 설정
# 1. 환경변수에서 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# 2. Streamlit 비밀 키 사용 (선택 사항: .streamlit/secrets.toml에 저장 가능)
if not api_key and "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]

# 3. 입력 받기 (API 키가 없는 경우)
if not api_key:
    api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

if not api_key:
    st.warning("OpenAI API 키를 입력하셔야 사용 가능합니다.")
    st.stop()

# API 키 설정
openai.api_key = api_key

# 🧠 앱 제목
st.title("🔬 생활 속 과학 질문 도우미")
st.write("궁금했던 과학적 현상, AI가 쉽게 설명해드립니다!")

# ❓ 사용자 질문 입력
question = st.text_input("💡 궁금한 점을 입력해보세요 (예: '전자레인지에 금속 넣으면 왜 안 되나요?')")

# 버튼 클릭 시 처리
if st.button("AI에게 물어보기") and question:
    with st.spinner("AI가 생각 중입니다..."):
        try:
            prompt = f"""
            당신은 일반인에게 과학을 쉽게 설명하는 친절한 과학 커뮤니케이터입니다.
            다음 질문에 대해 3~5문장 이내로 쉬운 한국어로 설명해주세요:

            질문: "{question}
