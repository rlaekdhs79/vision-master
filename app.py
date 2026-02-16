import streamlit as st
import google.generativeai as genai

st.title("🚀 인스타 떡상 AI 비서")

# Secrets에서 키 가져오기 (양쪽 공백 완벽 제거)
api_key = st.secrets["GOOGLE_API_KEY"].strip()

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # [핵심 수정] 404 에러 방지를 위해 모델 명칭만 정확히 입력
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("주제를 적어주세요")

        if st.button("문구 만들기"):
            if subject:
                # 콘텐츠 생성 시도
                response = model.generate_content(subject + " 인스타 문구 만들어줘")
                st.success("✅ 문구 생성 완료!")
                st.write(response.text)
            else:
                st.warning("주제를 입력해 주세요.")
                
    except Exception as e:
        # 에러 발생 시 상세 원인 출력
        st.error(f"연결 확인 중: {e}")
else:
    st.error("Secrets에 GOOGLE_API_KEY를 등록해 주세요!")
import streamlit as st
import google.generativeai as genai

st.title("🚀 인스타 떡상 AI 비서")

# Secrets에서 키 가져오기
api_key = st.secrets["GOOGLE_API_KEY"].strip()

if api_key:
    try:
        # 모델 설정 전파 방지
        genai.configure(api_key=api_key)
        
        # [핵심] 'models/' 접두사 없이 모델명만 사용
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("주제를 적어주세요")

        if st.button("문구 만들기"):
            if subject:
                # API 호출
                response = model.generate_content(subject + " 인스타 문구 만들어줘")
                st.success("✅ 문구 생성 완료!")
                st.write(response.text)
    except Exception as e:
        st.error(f"연결 확인 중: {e}")
