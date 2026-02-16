import streamlit as st
import google.generativeai as genai

# 1. 화면 설정
st.title("🚀 인스타 떡상 AI 비서")

# 2. 키 가져오기 (공백 제거까지 완벽하게)
api_key = st.secrets["GOOGLE_API_KEY"].strip()

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # 3. [핵심] 404 에러를 피하기 위한 가장 단순한 호출
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("주제를 적어주세요")

        if st.button("문구 만들기"):
            if subject:
                # 4. 가장 안전한 생성 방식
                response = model.generate_content(subject + " 인스타 문구 만들어줘")
                st.write(response.text)
            else:
                st.warning("주제를 입력하세요!")
                
    except Exception as e:
        st.error(f"에러 발생: {e}")
