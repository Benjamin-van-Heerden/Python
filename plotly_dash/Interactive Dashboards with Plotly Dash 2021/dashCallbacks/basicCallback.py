import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    id="main",
    children=[
        html.H3(
            id="heading",
            children="Basic Callback Example"
        ),
        html.Br(),
        dbc.Button(
            id="button",
            children="Click me",
            color="primary",
            n_clicks=0
        ),
        html.Br(),
        html.H3(
            id="output",
            children="default"
        )
    ],
    style={
        "display": "grid",
        "placeItems": "center",
    }
)

@app.callback(
    Output("output", "children"),
    [
        Input("button", "n_clicks")
    ]
)
def setStuff(n):
    return f"Button has been clicked {n} times"

    
if __name__ == '__main__':
    app.run_server(debug=True)


