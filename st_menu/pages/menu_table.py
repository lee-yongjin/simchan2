import pandas as pd
import streamlit as st

# 데이터 생성
data = {'이름': ['Alice', 'Bob', 'Charlie'],
        '나이': [25, 30, 35],
        '직업': ['개발자', '디자이너', 'PM']}

df = pd.DataFrame(data)

# Streamlit을 활용한 표 출력
st.title("데이터 테이블 예제")
st.dataframe(df)
