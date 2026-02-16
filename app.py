import streamlit as st
import google.generativeai as genai

# 페이지 기본 설정
st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서")
st.subheader("월 1,000만 원 수익을 위한 첫걸음")

# Secrets에서 API 키 가져오기
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        # 1. API 키 설정 (공백 제거 적용)
        genai.configure(api_key=api_key.strip())
        
        # 2. 최신형 무료 모델 연결
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        subject = st.text_input("어떤 주제로 문구를 만들까요?", key="subject_input")

        if st.button("✨ 떡상 문구 생성하기"):
            if subject:
                with st.spinner('AI 비서가 최고의 문구를 생성 중입니다...'):
                    # 3. 인스타 릴스 최적화 문구 생성
                    response = model.generate_content(f"{subject} 주제로 인스타그램 릴스에서 조회수가 잘 나올 문구를 이모지를 섞어서 만들어줘.")
                    st.success("✅ 문구 생성 완료!")
                    st.write(response.text)
            else:
                st.warning("주제를 입력해 주세요.")
                
    except Exception as e:
        # 에러 메시지를 더 구체적으로 파악하여 해결 가이드 제공
        st.error(f"시스템 연결 확인 중: {e}")
        st.info("💡 Tip: 구글 API 키를 새로 발급받으셨다면, 약 5~10분 정도 뒤에 다시 시도해 보세요.")
else:
    st.error("Secrets 설정에서 GOOGLE_API_KEY를 등록해 주세요!")
