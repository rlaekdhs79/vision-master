import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서 (무료 버전)")

# 1. 구글 키 설정 (Secrets 또는 입력창)
api_key = st.text_input("Google API 키를 넣어주세요", type="password", key="google_key")
if not api_key:
    api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

subject = st.text_input("주제 (예: 운동, 재테크)", key="subject_input")

if st.button("문구 만들기"):
    if api_key and subject:
        try:
            response = model.generate_content(f"{subject} 주제로 인스타 릴스 문구를 만들어줘")
            st.success(response.text)
        except Exception as e:
            st.error(f"에러가 발생했어요: {e}")
    else:
        st.warning("키와 주제를 확인해 주세요.")
