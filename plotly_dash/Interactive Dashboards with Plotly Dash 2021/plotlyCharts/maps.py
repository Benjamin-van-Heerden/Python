#%%
import plotly.express as px
from plotly.offline import init_notebook_mode, plot
init_notebook_mode()

df = px.data.election()

# %%
geojson = px.data.election_geojson()

fig = px.choropleth(
    df,
    geojson=geojson,
    locations="district",
    featureidkey="properties.district",
    projection="mercator",
    color="Bergeron"
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

# fig.show()
#plot(fig)
# %%
df = px.data.gapminder().query("year == 2007")

fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    color_continuous_scale=px.colors.sequential.Jet[::-1],
    title="Hi",
    hover_name="country",
    projection="orthographic"
)

#for colorscales available
#px.colors.sequential.swatches()

fig.show()
# %%
