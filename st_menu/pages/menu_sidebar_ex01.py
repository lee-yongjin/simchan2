import os
import streamlit as st
import pandas
import numpy

# st.sidebar의 모든 메서드 가져오기
methods = [method for method in dir(st.sidebar) if not method.startswith("_")]

# 메서드를 표 형식으로 출력
st.title("Streamlit Sidebar Methods")

# 표 데이터 생성
table_data = {"Method Name": methods}

# 데이터프레임을 활용한 표 출력
st.dataframe(table_data)
