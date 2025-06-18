import streamlit as st

try:
    import openai
except ImportError:
    st.error("❗ 'openai' 모듈이 설치되지 않았습니다. `pip install openai`를 실행해주세요.")
    st.stop()

import os

# API 키 설정
api_key = os.getenv("OPENAI_API_KEY")
if not api_key and "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]

if not api_key:
    api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

if not api_key:
    st.warning("API 키가 필요합니다.")
    st.stop()

openai.api_key = api_key

st.title("🎯 취미 기반 직업 추천 앱")
st.write("당신의 취미나 좋아하는 것을 입력하면 어울리는 직업과 설명을 알려드립니다.")

hobby = st.text_input("✨ 취미나 좋아하는 것을 입력해 주세요 (예: 사진 찍기, 요리하기)")

if st.button("추천 받기") and hobby:
    with st.spinner("AI가 직업을 추천 중입니다..."):
        try:
            prompt = f"""
            당신은 진로 상담 전문가입니다. 사용자가 입력한 취미나 좋아하는 활동을 바탕으로,
            가장 적합한 2~3개의 직업을 추천하고, 각 직업에 대해 2~3문장으로 간단하고 이해하기 쉽게 설명해 주세요.
            
            사용자 입력: "{hobby}"
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "너는 친절하고 이해하기 쉽게 진로를 상담해 주는 전문가야."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=600
            )

            answer = response["choices"][0]["message"]["content"]
            st.success("📝 추천 결과:")
            st.markdown(answer)

        except Exception as e:
            st.error("⚠️ 오류가 발생했습니다. API 키와 네트워크 상태를 확인해 주세요.")
            st.exception(e)
