import dash
import dash_core_components as dcc
import dash_html_components as html
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

app = dash.Dash()

app.layout = html.Div(
    id="main",
    children=[
        html.Div(
            id="heading",
            children=html.H1("Styling with HTML Components"),
            style={
                "textAlign": "center"
            }
        ),
        html.Div(
            id="barDiv",
            children=dcc.Graph(
                id="barGraph",
                figure=barChart(df1, df2, df3)
            ),
            style={
                "width": "50%",
                "display": "inline-block"
            }
        ),
        html.Div(
            id="lineDiv",
            children=dcc.Graph(
                id="lineGraph",
                figure=lineChart(df1, df2, df3)
            ),
            style={
                "width": "50%",
                "display": "inline-block"
            }
        ),
    ],
    style={
        "fontFamily": "sans-serif",
    }
)


if __name__ == "__main__":
    app.run_server(debug=True)