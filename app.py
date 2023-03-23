import streamlit as st
from PIL import Image

st.set_page_config(page_title="Streamlit-Indian Premier League (Cricket)")

st.title("Indian Premier League (Cricket)")

image = Image.open("static/images/ipl.jpg")
st.image(image, caption="IPL Image")

st.subheader("In this Web-App we are going to explore and analyze the Indian Premier League (Cricket) Stats")