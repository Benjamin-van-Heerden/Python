import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

navbar = dbc.Navbar(
    id="navbar",
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src=PLOTLY_LOGO, height="70px")
                ),
                dbc.Col(
                    dbc.NavbarBrand(
                        "App Title",
                        style={
                            "color": "black",
                            "fontSize": "35px",
                            "fontWeight": "500"
                        }
                    )
                )
            ],
            align="center",
            # no_gutters=True
        ),
        dbc.Button(
            id="button",
            children="Button",
            color="primary",
            className="ml-auto"
        )
    ]
)

app.layout = html.Div(
    id="main",
    children=[
        navbar
    ],
    style={
        "fontFamily": "Courier"
    }
)

if __name__ == "__main__":
    app.run_server(debug=True)
