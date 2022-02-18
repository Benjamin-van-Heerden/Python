import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.write("# Working with dataframes and json is easy!")

# Display data
df = sns.load_dataset("iris")

# Method 1
# st.dataframe(df)

# # Adding style
# st.dataframe(df.style.highlight_max(axis=0))

# # Method 2: Static table
# st.table(df)

# Method 3: Using superfunction st.write
st.write(df)

# Display json data
# st.json({"data": "name", "place": [1, 2, 3], "location": {"one": 2, "three": 4}})
# can also use write!
st.write({"data": "name", "place": [1, 2, 3], "location": {"one": 2, "three": 4}})

# display code:
code = """
const foo = () => {
    console.log("bar");
}
"""
st.code(code, language="javascript")