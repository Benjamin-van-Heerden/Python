import streamlit as st

# display images
from PIL import Image
from os.path import join, dirname

img = Image.open(join(dirname(__file__), "crossroads.jpg"))

st.image(img, use_column_width=True)

# from URL
st.image("https://yalebooks.yale.edu/sites/default/files/styles/book_jacket/public/imagecache/external/5259023800643532d3a3b9403db68928.jpg?itok=yG3lURpB")

# display videos
video_file = open(join(dirname(__file__), "crossroads.mp4"), "rb").read()
st.video(video_file, start_time=3)

# audio files
audio_file = open(join(dirname(__file__), "crossroads.mp4"), "rb").read()

st.audio(audio_file)