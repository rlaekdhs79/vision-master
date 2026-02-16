import streamlit as st
import google.generativeai as genai

# 1. 페이지 기본 설정
st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")
st.title("🚀 인스타 트렌드 AI 비서")
st.subheader("월 1,000만 원 수익을 위한 첫걸음")

# 2. Secrets에서 구글 API 키 가져오기
api_key = st.secrets.get("GOOGLE_API_KEY")

if api_key:
    try:
        # 3. 구글 AI 설정 및 모델 연결
        genai.configure(api_key=api_key)
        # 가장 빠르고 똑똑한 최신 무료 모델
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 4. 사용자 입력창
        subject = st.text_input("어떤 주제로 문구를 만들까요? (예: 다이어트, 부업)", key="subject_input")

        # 5. 실행 버튼
        if st.button("✨ 떡상 문구 생성하기"):
            if subject:
                with st.spinner('AI 비서가 문구를 작성 중입니다...'):
                    # AI에게 인스타용 문구 요청
                    prompt = f"인스타그램 릴스에서 반응이 좋을만한 {subject} 관련 문구를 이모지를 섞어서 3가지 버전으로 만들어줘."
                    response = model.generate_content(prompt)
                    
                    st.success("✅ 문구 생성 완료!")
                    st.write(response.text)
                    st.divider()
                    st.info("💡 위 문구를 복사해서 인스타에 올리고 수익을 창출해 보세요!")
            else:
                st.warning("주제를 입력해 주세요.")
                
    except Exception as e:
        # 에러 발생 시 상세 내용 출력 (400, 404 에러 방지용)
        st.error(f"연결에 문제가 생겼습니다: {e}")
        st.info("Tip: Secrets에 키가 정확히 입력되었는지, 혹은 5분 정도 지났는지 확인해 주세요.")
else:
    st.error("Secrets 설정에서 'GOOGLE_API_KEY'를 먼저 등록해 주세요!")
