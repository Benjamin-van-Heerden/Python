# %%
import plotly.graph_objects as go
import plotly.express as px

from plotly.offline import init_notebook_mode, plot
init_notebook_mode()

df1 = px.data.gapminder().query("country == 'South Africa'")
df2 = px.data.gapminder().query("country == 'India'")
df3 = px.data.gapminder().query("country == 'United States'")
# %%
data = [
    go.Bar(
        x=df1["year"],
        y=df1["gdpPercap"],
        marker_color="red",
        name="South Africa"
    ),
    go.Bar(
        x=df2["year"],
        y=df2["gdpPercap"],
        marker_color="blue",
        name="India"
    ),
    go.Bar(
        x=df3["year"],
        y=df3["gdpPercap"],
        marker_color="green",
        name="US"
    )
]

layout = go.Layout(
    title="GDP per capita per year",
    xaxis_title="Years",
    yaxis_title="GDP per capita",
    barmode="group"
)

fig = go.Figure(data=data, layout=layout)
fig.show()
# %%
