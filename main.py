import streamlit as st
import openai
import os

# 🔑 OpenAI API 키 설정 (환경변수 또는 직접 입력)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# 앱 제목
st.title("🔬 생활 속 과학 질문 도우미")
st.write("궁금했던 과학적 원리를 AI가 쉽게 설명해드립니다!")

# 사용자 입력
question = st.text_input("❓ 궁금한 점을 입력하세요 (예: '전자레인지에 금속 넣으면 왜 안 되나요?')")

# 버튼 클릭 시 응답 생성
if st.button("설명해줘") and question:
    with st.spinner("AI가 과학적으로 설명 중..."):
        try:
            prompt = f"""
            당신은 대중에게 과학을 쉽게 설명해주는 친절한 과학 커뮤니케이터입니다.
            아래 사용자의 질문에 대해 3~5문장으로 쉬운 한국어로 설명해주세요.
            질문: {question}
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # 또는 'gpt-4' (계정에 따라 다름)
                messages=[
                    {"role": "system", "content": "너는 과학 설명을 잘하는 전문가야."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            answer = response['choices'][0]['message']['content']
            st.success("🧠 AI의 과학 설명:")
            st.write(answer)

        except Exception as e:
            st.error("에러가 발생했습니다. API 키를 확인하거나 네트워크를 점검해주세요.")
            st.exception(e)

# 하단 안내
st.markdown("---")
st.markdown("👨‍🔬 만든 사람: [당신의 이름] | 📘 Powered by OpenAI | 🌐 Streamlit으로 제작")
