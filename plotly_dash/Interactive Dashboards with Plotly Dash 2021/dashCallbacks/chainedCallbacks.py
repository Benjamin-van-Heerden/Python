import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from pandas._config.config import options

options_all = {
    "America": ["NY", "SF", "CIN"],
    "South Africa": ["PTA", "CPT", "JB"]
}

df = pd.DataFrame(options_all)

app = dash.Dash()

app.layout = html.Div(
    id="main",
    children=[
        dcc.Dropdown(
            id="countries",
            options=[{"label": c, "value": c} for c in df.columns],
            value="America"
        ),
        html.Br(),
        dcc.Dropdown(
            id="cities"
        ),
        html.Br(),
        html.Div(
            id="displaySelections"
        )
    ]
)

@app.callback(
    Output("cities", "options"),
    [
        Input("countries", "value")
    ]
)
def setCities(country):
    return [{"label": c, "value": c} for c in df[country]]

@app.callback(
    Output("cities", "value"),
    [
        Input("cities", "options")
    ]
)
def setCityDefault(cities):
    return cities[0]["value"]


@app.callback(
    Output("displaySelections", "children"),
    [
        Input("countries", "value"),
        Input("cities", "value")
    ]
)
def setOutput(country, city):
    return f"""The country is {country}
    The city is {city}"""

if __name__ == "__main__":
    app.run_server(debug=True)