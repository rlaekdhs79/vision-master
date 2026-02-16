import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서 (무료 버전)")

# 구글 API 키 설정 (Secrets에서 가져옴)
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # 최신형 무료 엔진으로 교체 완료
    model = genai.GenerativeModel('gemini-1.5-flash')

    subject = st.text_input("주제 (예: 운동, 재테크)", key="subject_input")

    if st.button("문구 만들기"):
        if subject:
            try:
                response = model.generate_content(f"{subject} 주제로 인스타 릴스 문구를 만들어줘")
                st.success(response.text)
            except Exception as e:
                st.error(f"에러가 발생했어요: {e}")
        else:
            st.warning("주제를 입력해 주세요.")
else:
    st.error("Secrets에 GOOGLE_API_KEY를 먼저 등록해 주세요!")
