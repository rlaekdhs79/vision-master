import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="인스타 트렌드 AI 비서", layout="centered")

st.title("🚀 인스타 트렌드 AI 비서")
st.write("유행하는 릴스 주제를 찾고 떡상 문구를 만드세요.")

# 1. 키 설정 (화면 입력 우선, 없으면 Secrets 확인)
# 중복 방지를 위해 key="api_key_input"을 추가했습니다.
api_key = st.text_input("OpenAI API 키를 제공해 주세요", type="password", key="api_key_input")
if not api_key:
    api_key = st.secrets.get("OPENAI_API_KEY")

# 2. 주제 입력창
subject = st.text_input("주제 (예: 운동, 재테크)", key="subject_input")

# 3. 문구 생성 로직
if st.button("문구 만들기"):
    if api_key and subject:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"{subject} 주제로 인스타 릴스 문구를 만들어 주세요"}]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"에러가 일어났어요: {e}")
    else:
        st.warning("키와 주제를 모두 확인해 주세요.")
