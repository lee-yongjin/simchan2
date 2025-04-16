import streamlit as st

# st.sidebar의 모든 메서드 가져오기
methods = [method for method in dir(st.sidebar) if not method.startswith("_")]

# 각 메서드의 간단한 사용법을 제공하는 딕셔너리 (일부 예제 포함)
usage_examples = {
    "button": "st.sidebar.button(label)",
    "checkbox": "st.sidebar.checkbox(label)",
    "radio": "st.sidebar.radio(label, options)",
    "selectbox": "st.sidebar.selectbox(label, options)",
    "slider": "st.sidebar.slider(label, min_value, max_value, value)",
    "text_input": "st.sidebar.text_input(label, value='')",
    "number_input": "st.sidebar.number_input(label, min_value, max_value, value)",
    "color_picker": "st.sidebar.color_picker(label, value='#000000')"
}

# 메서드와 사용법을 표 형식으로 출력
st.title("Streamlit Sidebar Methods & Usage")

# 표 데이터 생성
table_data = {
    "Method Name": methods,
    "Usage Example": [usage_examples.get(m, "st.sidebar." + m + "(...)") for m in methods]
}

# 데이터프레임을 활용한 표 출력
st.dataframe(table_data)