import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from os.path import join, dirname


df = pd.read_csv(join(dirname(__file__), "../course_materials_learnstreamlit/LearnStreamlit/Module01/data/prog_languages_data.csv"))

st.title("Plotting in streamlit with plotly")

st.dataframe(df)

fig = px.pie(df, values="Sum", names="lang", title="Pie chart of programming languages")
st.plotly_chart(fig)

fig2 = px.bar(df, x="lang", y="Sum")
st.plotly_chart(fig2)