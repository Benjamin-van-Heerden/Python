import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import numpy as np
from pandas.core.indexes import multi
import plotly.express as px

df = px.data.gapminder()

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div(
    id="main",
    children=[
        dcc.Slider(
            id="yearSlider",
            min=df["year"].min(),
            max=df["year"].max(),
            value=df["year"].min(),
            marks={str(year): str(year) for year in df["year"].unique()},
            step=None
        ),
        html.Br(),
        dcc.Dropdown(
            id="continentDropdown",
            options=[{"label": con, "value": con} for con in df["continent"].unique()],
            value=[con for con in df["continent"].unique()],
            multi=True
        ),
        html.Br(),
        html.Div(
            id="filtersSelected",
            style={
                "textAlign": "center"
            }
        ),
        html.Br(),
        dcc.Graph(
            id="scatterPlot"
        )
    ],
    style={
        "padding": "20px"
    }
)    

@app.callback(
    Output("filtersSelected", "children"),
    Output("scatterPlot", "figure"),
    [
        Input("yearSlider", "value"),
        Input("continentDropdown", "value"),
    ]
)
def updateFilters(year, continents):
    filtersList = []
    filtersList.append(html.Li(f"Year Selected: {year}"))
    for con in continents:
        filtersList.append(html.Li(f"Continent Selected: {con}"))
    divResult = html.Ol(children=filtersList)

    filterDf = df[df["year"] == year]
    filterDf = filterDf[filterDf["continent"].isin(continents)]
    fig = px.scatter(
        filterDf, 
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        range_x=[100, 100000],
        range_y=[25, 90],
        title=f"GDP Per Capita For {year}",
        size_max=50
    )
    return divResult, fig

if __name__ == '__main__':
    app.run_server(debug=True)