import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

cardContent = [
    dbc.CardHeader("Card Header"),
    dbc.CardBody(
        [
            html.H5("Card Title", className="card-title"),
            html.P("This is some card content that we will use",
                   className="card-text")
        ]
    )
]

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(cardContent, color="primary", inverse=True)
                ),
                dbc.Col(
                    dbc.Card(cardContent, color="info", inverse=True)
                ),
                dbc.Col(
                    dbc.Card(cardContent, color="warning", inverse=True)
                )
            ]
        )
    ],
    fluid=True,
    style={
        "padding": "10px",
        "width": "calc(100% - 20px)"
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
