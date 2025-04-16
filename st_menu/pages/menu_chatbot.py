import streamlit as st

st.title("🌟 예쁜 챗봇 🌟")
st.write("💬 저는 여러분과 대화를 나누는 AI 챗봇입니다!")

user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    st.write(f"사용자 입력: {user_input}")
