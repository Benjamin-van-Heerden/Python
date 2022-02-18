import streamlit as st
from os.path import join, dirname
from PIL import Image
# config must be the first activity!
img = Image.open(join(dirname(__file__), "crossroads.jpg"))

st.set_page_config(
    page_title="Hello",
    page_icon=img, # emoji's also work well here
    layout="wide",
    initial_sidebar_state="expanded"
)

st.write("Hello")
if st.sidebar.button("Menu"):
    st.write("button clicked")

st.write(dir(st))