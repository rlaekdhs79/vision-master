import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서(무료 버전)")

# 1. 구글 API 키 설정 (Secrets에서 안전하게 가져오기)
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # 2. 최신 요리 창고(v1beta)와 연결하는 설정
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("주제 (예: 운동, 재테크)", key="subject_input")

        if st.button("문구 만들기"):
            if subject:
                # 3. 인스타 떡상 문구 생성 요청
                response = model.generate_content(f"{subject} 주제로 인스타 릴스 문구를 만들어줘")
                st.success(response.text)
            else:
                st.warning("주제를 입력해 주세요.")
    except Exception as e:
        st.error(f"에러가 발생했어요: {e}")
else:
    st.error("Secrets에 GOOGLE_API_KEY를 등록해 주세요!")
