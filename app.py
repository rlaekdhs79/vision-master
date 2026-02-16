import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서")
st.subheader("월 1,000만 원 수익을 위한 첫걸음")

api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        # 1. API 설정
        genai.configure(api_key=api_key)
        
        # 2. 모델 설정 (접두사 'models/'를 명시적으로 제거하고 호출)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("어떤 주제로 문구를 만들까요?", key="subject_input")

        if st.button("✨ 떡상 문구 생성하기"):
            if subject:
                with st.spinner('AI 비서가 작업 중...'):
                    # 3. 콘텐츠 생성
                    response = model.generate_content(f"{subject} 주제로 인스타그램 릴스 문구를 짧고 강력하게 만들어줘.")
                    st.success("✅ 문구 생성 완료!")
                    st.write(response.text)
            else:
                st.warning("주제를 입력해 주세요.")
                
    except Exception as e:
        # 에러 발생 시 상세 원인 출력
        st.error(f"연결에 문제가 생겼습니다: {e}")
else:
    st.error("Secrets에 GOOGLE_API_KEY를 등록해 주세요!")
