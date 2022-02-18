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
    go.Scatter(
        x=df1["year"],
        y=df1["lifeExp"],
        name="South Africa",
        mode="lines+markers",
        line={
            "color": "black",
            "width": 10
        },
        marker={
            "color": "red",
            "size": 15
        },
        text=df1["gdpPercap"]
    ),
    go.Scatter(
        x=df2["year"],
        y=df2["lifeExp"],
        marker_color="blue",
        name="India",
        mode="lines+markers"
    ),
    go.Scatter(
        x=df3["year"],
        y=df3["lifeExp"],
        marker_color="green",
        name="US",
        mode="lines+markers"
    )
]

layout = go.Layout(
    title="Life expectancy per year",
    xaxis_title="Years",
    yaxis_title="Life Expectancy",
    hovermode="closest"
)

fig = go.Figure(data=data, layout=layout)
fig.show()
# plot(fig)
#^^for browser output
# %%
