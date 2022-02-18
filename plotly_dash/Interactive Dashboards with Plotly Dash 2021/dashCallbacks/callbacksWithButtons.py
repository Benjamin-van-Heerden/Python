import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    id="main",
    children=[
        dbc.Button(
            id="button",
            children="This is a button",
            n_clicks=0,
            color="warning"
        ),
        html.Br(),
        html.H1(
            id="output"
        )
    ],
    style={
        "padding-top": "20px",
        "display": "grid",
        "placeItems": "center"
    }
)

@app.callback(
    Output("output", "children"),
    [
        Input("button", "n_clicks")
    ]
)
def buttonUpdate(value):
    return f"Has been clicked {value} times"

if __name__ == '__main__':
    app.run_server(debug=True)