import pandas as pd

# pandas의 주요 객체 선택
pandas_objects = [pd.DataFrame, pd.Series]

# 각 객체의 메서드와 사용법 수집
data = []
for obj in pandas_objects:
    methods = [method for method in dir(obj) if not method.startswith("_")]
    for method in methods:
        example = f"pd.{obj.__name__}().{method}(...)"
        data.append((obj.__name__, method, example))

# Streamlit을 활용하여 표 형식으로 출력
import streamlit as st

st.title("Pandas Methods & Usage Examples")

# 데이터프레임 생성 및 출력
df = pd.DataFrame(data, columns=["Pandas Object", "Method Name", "Usage Example"])
st.dataframe(df)
