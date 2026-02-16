import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정
st.set_page_config(page_title="인스타 떡상 AI 비서")
st.title("🚀 인스타 떡상 AI 비서")

# 2. API 키 설정
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key.strip())
        # [핵심] 404 에러 방지를 위한 표준 모델 명칭
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # [중요] Duplicate ID 에러 방지를 위해 key="unique_input" 추가
        subject = st.text_input("주제를 적어주세요", key="unique_input")

        if st.button("문구 만들기", key="unique_button"):
            if subject:
                with st.spinner('AI가 고민 중입니다...'):
                    response = model.generate_content(subject + " 인스타 릴스 문구 만들어줘")
                    st.success("✅ 완료!")
                    st.write(response.text)
            else:
                st.warning("주제를 입력하세요.")
                
    except Exception as e:
        st.error(f"연결 확인 중: {e}")
else:
    st.error("Secrets에 API 키를 등록해 주세요!")
