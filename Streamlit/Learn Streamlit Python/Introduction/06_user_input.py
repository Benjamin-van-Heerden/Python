import streamlit as st



# text input
first_name = st.text_input('First Name:')
password = st.text_input('Password:', type='password')

# text area
last_name = st.text_area('Last Name:', height=200)

# number
number = st.number_input("Favourite number:", 1, 100)

# date
date = st.date_input("Birthday:")

# time
time = st.time_input("Time:")

# color
color = st.color_picker("Color:")

with st.expander("Show Inputs"):
    st.header(f"Your first name is: {first_name}")
    st.header(f"Your last name is: {last_name}")
    st.header(f"Your number is: {number}")
    st.header(f"Your date and time is: {date} {time}")