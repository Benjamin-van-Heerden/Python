# %%
# Scatter and Line plots are the same thing, only the mode changes
import plotly.graph_objects as go
import plotly.express as px

from plotly.offline import init_notebook_mode, plot
init_notebook_mode()

df = px.data.gapminder().query("year == 2007")

fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=50
)

fig.show()
# %%
