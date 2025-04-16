from PIL import Image, ImageDraw
import streamlit as st

# 이미지 생성
img = Image.new('RGB', (200, 200), (255, 255, 255))
draw = ImageDraw.Draw(img)
draw.rectangle([(50, 50), (150, 150)], fill=(255, 0, 0))

# Streamlit에서 이미지 출력
st.title("이미지 생성 예제")
st.image(img, caption="빨간색 사각형 그림")

