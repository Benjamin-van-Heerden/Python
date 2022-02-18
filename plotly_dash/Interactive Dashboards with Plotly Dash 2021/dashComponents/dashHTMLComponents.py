import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    id="main",
    children=[
        # H1
        html.H1(
            id="H1",
            children="This is H1",
            style={
                "textAlign": "center",
            }
        ),

        # H2
        html.H2(
            id="H2",
            children="This is H2",
            style={
                "textAlign": "center",
            }
        ),

        # Paragraph
        html.P(
            id="para",
            children="This is paragraph",
            style={
                "textAlign": "center",
            }
        ),

        # Link (Div for alignment)
        html.Div(
            id="linkContainer",
            children=html.A(
                id="link",
                children="This is link",
                href="http://www.udemy.com/",
                style={
                    "fontSize": 30
                }
            ),
            style={
                "textAlign": "center",
            }
        ),

        # Line break
        html.Br(),

        # Image (Div for alignment)
        html.Div(
            id="imageContainer",
            children=html.Img(
                id="img",
                src="https://s.udemycdn.com/meta/default-meta-image-v2.png",
                height="50px"
            ),
            style={
                "display": "grid",
                "placeItems": "center" 
            }
        ),

        # Rolling Text
        html.Marquee(
            id="marquee",
            children="This can be used for notifications"
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
