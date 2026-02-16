import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서 (무료 버전)")

# 1. 구글 API 키 설정 (Secrets 확인)
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # 2. 가장 안정적인 기본 모델 설정 사용
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("주제 (예: 운동, 재테크)", key="subject_input")

        if st.button("문구 만들기"):
            if subject:
                # 3. 텍스트 생성 요청
                response = model.generate_content(subject + " 주제로 인스타 릴스 문구를 짧고 강력하게 만들어줘")
                if response.text:
                    st.success(response.text)
                else:
                    st.warning("결과를 가져오지 못했습니다. 다시 시도해 주세요.")
            else:
                st.warning("주제를 입력해 주세요.")
    except Exception as e:
        # 404 에러 등을 방지하기 위한 상세 에러 메시지 출력
        st.error(f"시스템 연결 확인 중: {e}")
else:
    st.error("Secrets에 GOOGLE_API_KEY를 등록해 주세요!")
