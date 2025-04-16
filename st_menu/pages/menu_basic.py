import streamlit as st

st.title("나의 첫 Streamlit 앱")
st.write("Hello, Streamlit!")

st.write("------------------------------------------------")

st.title("타이틀입니다")
st.header("헤더입니다")
st.subheader("서브헤더입니다")
st.text("기본 텍스트입니다")
st.markdown("**마크다운** 형식의 텍스트")
st.code("print('Hello')", language="python")

st.write("------------------------------------------------")

name = st.text_input("이름을 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
hobby = st.text_area("취미를 적어주세요")
agree = st.checkbox("동의합니다")
gender = st.radio("성별", ["남성", "여성", "기타"])
color = st.selectbox("좋아하는 색", ["빨강", "파랑", "초록"])
colors = st.multiselect("좋아하는 색들", ["빨강", "파랑", "초록"])
level = st.slider("레벨을 선택하세요", 1, 100, 50)
file = st.file_uploader("파일을 업로드하세요")

st.write("------------------------------------------------")

if st.button("클릭하세요"):
    st.write("버튼이 눌렸습니다!")

if st.toggle("토글 스위치"):
    st.write("토글이 켜졌어요!")

if st.download_button("데이터 다운로드", data="예시 데이터", file_name="data.txt"):
    st.write("다운로드 완료")

st.write("------------------------------------------------")

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.write("------------------------------------------------")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)

st.write("------------------------------------------------")

#import plotly.express as px
#df = px.data.iris()
#fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
#st.plotly_chart(fig)

st.write("------------------------------------------------")

col1, col2 = st.columns(2)

with col1:
    st.write("왼쪽 컬럼입니다")

with col2:
    st.write("오른쪽 컬럼입니다")


st.write("------------------------------------------------")

with st.expander("자세히 보기"):
    st.write("숨겨진 내용을 여기에...")

st.write("------------------------------------------------")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("증가"):
    st.session_state.count += 1

st.write(f"카운트: {st.session_state.count}")

st.write("------------------------------------------------")

message = st.chat_input("메시지를 입력하세요")

if message:
    with st.chat_message("user"):
        st.markdown(message)

st.write("------------------------------------------------")

st.progress(50)
st.spinner("로딩 중입니다...")
#st.balloons()
st.toast("작업 완료!")

