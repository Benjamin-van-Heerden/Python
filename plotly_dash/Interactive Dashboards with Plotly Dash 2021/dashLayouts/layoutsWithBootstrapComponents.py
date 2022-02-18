import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

df1 = px.data.gapminder().query("country == 'South Africa'")
df2 = px.data.gapminder().query("country == 'India'")
df3 = px.data.gapminder().query("country == 'United States'")


def barChart(df1, df2, df3):
    data = [
        go.Bar(
            x=df1["year"],
            y=df1["gdpPercap"],
            marker_color="red",
            name="South Africa"
        ),
        go.Bar(
            x=df2["year"],
            y=df2["gdpPercap"],
            marker_color="blue",
            name="India"
        ),
        go.Bar(
            x=df3["year"],
            y=df3["gdpPercap"],
            marker_color="green",
            name="US"
        )
    ]

    layout = go.Layout(
        title="GDP Per Capita By Year",
        xaxis_title="Year",
        yaxis_title="GDP Per Capita",
        barmode="group"
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


def lineChart(df1, df2, df3):
    data = [
        go.Scatter(
            x=df1["year"],
            y=df1["lifeExp"],
            name="South Africa",
            mode="lines+markers",
            line={
                "color": "black",
                "width": 10
            },
            marker={
                "color": "red",
                "size": 15
            },
            text=df1["gdpPercap"]
        ),
        go.Scatter(
            x=df2["year"],
            y=df2["lifeExp"],
            marker_color="blue",
            name="India",
            mode="lines+markers"
        ),
        go.Scatter(
            x=df3["year"],
            y=df3["lifeExp"],
            marker_color="green",
            name="US",
            mode="lines+markers"
        )
    ]

    layout = go.Layout(
        title="Life Expectancy By Year",
        xaxis_title="Years",
        yaxis_title="Life Expectancy",
        hovermode="closest"
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.H1(
                        id="h1",
                        children="Styling Using Bootstrap Components"
                    ),
                    xl=12,
                    lg=12,
                    md=12,
                    sm=12,
                    xs=12
                )
            ],
            style={
                "textAlign": "center",
                "marginTop": "30px",
                "marginBottom": "30px"
            }
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="barChart",
                        figure=barChart(df1, df2, df3)
                    ),
                    xl=6,
                    lg=6,
                    md=6,
                    sm=12,
                    xs=12
                ),
                dbc.Col(
                    dcc.Graph(
                        id="lineChart",
                        figure=lineChart(df1, df2, df3)
                    ),
                    xl=6,
                    lg=6,
                    md=6,
                    sm=12,
                    xs=12
                )
            ]
        )
    ],
    fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=True)
