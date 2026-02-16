import streamlit as st
import openai

# 페이지 설정
st.set_page_config(page_title="인스타 비전 마스터", page_icon="📸")

st.title("🚀 인스타 트렌드 AI 비서")
st.write("유행하는 릴스 주제를 찾고 떡상 문구를 만드세요.")

# 1. 트렌드 섹션 (실제 구현 시 데이터 연동)
st.header("🔥 오늘의 릴스 트렌드")
if st.button("실시간 유행 확인"):
    st.success("1위: 오운완 챌린지 / 2위: 데스크테리어 / 3위: 갓생살기")

# 2. AI 문구 생성기
st.header("📝 AI 전략 문구 생성")
api_key = st.text_input("OpenAI API 키를 넣어주세요", type="password")
topic = st.text_input("주제 (예: 운동, 재테크)")

if st.button("문구 만들기"):
    if api_key and topic:
        openai.api_key = api_key
        prompt = f"인스타그램 '{topic}' 주제로 사람들의 저장을 유도하는 릴스 캡션을 써줘."
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        st.info(response.choices[0].message.content)
    else:
        st.warning("키와 주제를 모두 입력해주세요.")