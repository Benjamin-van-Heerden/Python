import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder().query("year == 2007")

fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    color_continuous_scale=px.colors.sequential.Jet[::-1],
    title="Life Expectancy By Country",
    hover_name="country",
    projection="orthographic"
)

fig.update_layout(
    width=1000,
    height=800
)

app = dash.Dash()

app.layout = html.Div(
    id="main",
    children=[
        html.Div(
            html.H1(
                id="heading1",
                children="Styling using html components"
            ),
            style={
                    "textAlign": "center",
                    "fontFamily": "sans-serif"
                }
        ),
        html.Div(
            dcc.Graph(
                id="worldMap",
                figure=fig,
            ),
            style={
                "width": "60%",
                "height": "50%",
                "alignSelf": "center"
            }
        )
    ],
    style={
        "height": "calc(100vh - 40px)",
        "width": "calc(100vw - 40px)",
        "position": "absolute",
        "top": "0",
        "left": "0",
        "backgroundColor": "lightgrey",
        "padding": "20px",
        "display": "flex",
        "flexDirection": "column"
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
