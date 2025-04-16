import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
fig, ax = plt.subplots()
ax.plot(x, y, label="Sine Wave")
ax.legend()
ax.set_title("Sin 그래프")

# Streamlit에서 차트 출력
st.title("차트 예제")
st.pyplot(fig)

