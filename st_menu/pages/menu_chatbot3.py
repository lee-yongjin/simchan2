import streamlit as st
import random

# Streamlit 페이지 설정
st.set_page_config(page_title="심플한 챗봇", layout="wide")

# 응답 예제
responses = [
    "안녕하세요! 😊",
    "오늘 하루는 어땠나요?",
    "저는 여러분과 대화하는 것을 좋아해요!",
    "흥미로운 질문이네요! 더 알려주세요.",
    "저도 그렇게 생각해요! 😄"
]

# 대화 기록 상태 관리
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 타이틀
st.title("심플한 챗봇 🤖")
st.subheader("AI와 함께하는 대화")

# 대화 출력 (과거 메시지 출력)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 입력 폼
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("메시지를 입력하세요:", placeholder="예: 오늘 날씨 어때?")
    submit_button = st.form_submit_button("전송")

# 사용자 입력 처리
if submit_button and user_input:
    # 사용자 메시지 저장
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # 챗봇 응답 생성
    chatbot_response = random.choice(responses)
    st.session_state.chat_history.append({"role": "assistant", "content": chatbot_response})
    
    # 새 메시지 출력
    with st.chat_message("assistant"):
        st.write(chatbot_response)
        