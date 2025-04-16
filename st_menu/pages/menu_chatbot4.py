import streamlit as st

st.title("chat_input 챗봇")
st.write("저는 여러분과 대화를 나누는 AI 챗봇입니다!")

# 초기 메시지 기록
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 메시지 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    # 사용자 메시지 저장 및 표시
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 챗봇 응답 (여기서는 예시로 간단한 반응)
    response = f"'{user_input}'에 대한 응답입니다."

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
