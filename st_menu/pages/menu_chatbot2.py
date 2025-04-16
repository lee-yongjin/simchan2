import streamlit as st
import random

# 챗봇의 간단한 응답 예제
responses = [
    "안녕하세요! 😊",
    "오늘 기분은 어떠세요?",
    "무엇을 도와드릴까요?",
    "좋은 하루 보내세요! 🌸",
    "흥미로운 질문이네요! 더 알려주세요."
]

# Streamlit 설정
st.set_page_config(page_title="예쁜 챗봇", layout="wide")

# 대화 저장을 위한 상태 관리
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 입력값 저장용 임시 상태 변수
if "temp_input" not in st.session_state:
    st.session_state.temp_input = ""

st.title("🌟 예쁜 챗봇 🌟")
st.write("💬 저는 여러분과 대화를 나누는 AI 챗봇입니다!")

# 대화 출력 (위쪽에 위치)
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력 (하단에 위치)
user_input = st.text_input("메시지를 입력하세요:", value=st.session_state.temp_input, key="user_input")

# 메시지 전송 버튼 추가
if st.button("전송"):
    if user_input:
        # 챗봇 응답 생성
        chatbot_response = random.choice(responses)

        # 대화 기록 저장
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": chatbot_response})

        # 입력값 초기화
        st.session_state.temp_input = ""  # temp_input을 통해 입력값 관리

        