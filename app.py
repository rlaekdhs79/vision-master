import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서 (무료 버전)")

# 1. 구글 API 키 설정
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # [핵심 수정] 모델 명칭을 가장 호환성이 높은 버전으로 고정했습니다.
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        
        subject = st.text_input("주제 (예: 운동, 재테크)", key="subject_input")

        if st.button("문구 만들기"):
            if subject:
                # 생성 요청 시 안전하게 텍스트만 추출하도록 설정
                response = model.generate_content(subject + " 주제로 인스타 릴스 문구를 만들어줘")
                st.success(response.text)
            else:
                st.warning("주제를 입력해 주세요.")
    except Exception as e:
        # 에러 메시지를 통해 구체적인 원인 파악 (404 방지)
        st.error(f"시스템 연결 상태: {e}")
else:
    st.error("Secrets에 GOOGLE_API_KEY를 먼저 등록해 주세요!")
