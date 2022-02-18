import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


app = dash.Dash()

app.layout = html.Div(
    id="main",
    children=[
        dcc.Input(
            id="input1",
            type="text",
            value="Montreal"
        ),
        dcc.Input(
            id="input2",
            type="text",
            value="Canada"
        ),
        dbc.Button(
            id="submit",
            type="submit",
            children="Submit",
            n_clicks=0
        ),
        html.Div(
            id="output"
        )
    ],
    style={
        "padding": "20px",
        "display": "grid",
        "placeItems": "center"
    }
)

@app.callback(
    Output("output", "children"),
    [
        Input("submit", "n_clicks"),
    ],
    [
        State("input1", "value"),
        State("input2", "value"),
    ]
)
def update(n_clicks, input1, input2):
    return f"""The button has been pressed {n_clicks} times
    input1: {input1}
    input2: {input2}
    """

if __name__ == '__main__':
    app.run_server(debug=True)