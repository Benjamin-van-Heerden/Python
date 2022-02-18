import streamlit as st

# buttons
name = "Ben"
if st.button("Submit"):
    st.write(f"Name: {name}")

if st.button("Submit", key="Submit01"):
    st.write(f"Name: {name}")

# radio buttons
status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success(f"You are active")
elif status == "Inactive":
    st.warning(f"You are inactive")

# checkbox
if st.checkbox("Show/Hide"):
    st.write(f"Showing something...")

# expander
with st.expander("Python"):
    st.success(f"Hello Python")

# select
my_languages = ["Python", "Scala", "JavaScript"]

choice = st.selectbox("language", my_languages)

st.warning(f"You selected: {choice}")

# multi-select
spoken_lang = ["English", "Spanish", "Afrikaans"]
my_lang = st.multiselect("spoken lang", spoken_lang, default="English")

with st.expander("Spoken Languages"):
    st.write(f"Spoken languages are {my_lang}")

# slider (numbers only)
age = st.slider("Age", 1, 100, 5)

# select slider (any)
colors = ["yellow", "green", "red", "black", "white"]
color = st.select_slider(
    "Choose color", options=colors, help="hi"
)

# a bit more complex example
defaults = st.selectbox("Choose defaults",
                        [
                            {"name": "Zeros",
                             "slider1": 0,
                             "slider2": 0
                            },
                            {"name": "Two and three",
                             "slider1": 2,
                             "slider2": 3
                            },
                        ],
                        format_func=lambda option:option["name"]
)

slider = st.slider("set value", min_value=0, value=defaults["slider1"], max_value=10)

st.write(f"Slider value: {slider}")

slider_2 = st.slider("set value 2", min_value=0, value=defaults["slider2"], max_value=10)

st.write(f"Slider value: {slider_2}")

