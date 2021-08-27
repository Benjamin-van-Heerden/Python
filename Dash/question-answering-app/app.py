from transformers import pipeline
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
from dash.dependencies import Input, Output, State

IMAGE_URL = "https://www.smartdatacollective.com/wp-content/uploads/2018/03/Natural-Language-Processing-NLP-AI.jpg"
DEFAULT_CONTEXT = """John Fitzgerald Kennedy (May 29, 1917 – November 22, 1963), often referred to by his initials JFK, was an American politician who served as the 35th president of the United States from 1961 until his assassination near the end of his third year in office. Kennedy served at the height of the Cold War, and the majority of his work as president concerned relations with the Soviet Union and Cuba. A member of the Kennedy family and a Democrat, he represented Massachusetts in both houses of the U.S. Congress prior to becoming president.

Kennedy graduated from Harvard University in 1940 before joining the U.S. Naval Reserve the following year. During World War II, he commanded a series of PT boats in the Pacific theater and earned the Navy and Marine Corps Medal for his service and war heroism. After a brief stint in journalism, Kennedy represented a working-class Boston district in the U.S. House of Representatives from 1947 to 1953. He was subsequently elected to the U.S. Senate and served as the junior senator for Massachusetts from 1953 to 1960. While in the Senate, Kennedy published his book, Profiles in Courage, which won a Pulitzer Prize. In the 1960 presidential election, he narrowly defeated Republican opponent Richard Nixon, who was the incumbent vice president. Kennedy's humor, charm, and youth in addition to his father's money and contacts were great assets in the campaign. Kennedy's campaign gained momentum after the first televised presidential debates in American history. Kennedy was the first Catholic elected president.

Kennedy's administration included high tensions with communist states in the Cold War. As a result, he increased the number of American military advisers in South Vietnam. The Strategic Hamlet Program began in Vietnam during his presidency. In April 1961, he authorized an attempt to overthrow the Cuban government of Fidel Castro in the failed Bay of Pigs Invasion.[2] Kennedy authorized the Cuban Project in November 1961. He rejected Operation Northwoods (plans for false flag attacks to gain approval for a war against Cuba) in March 1962. However, his administration continued to plan for an invasion of Cuba in the summer of 1962.[3] The following October, U.S. spy planes discovered Soviet missile bases had been deployed in Cuba; the resulting period of tensions, termed the Cuban Missile Crisis, nearly resulted in the breakout of a global thermonuclear conflict. He also signed the first nuclear weapons treaty in October 1963. Kennedy presided over the establishment of the Peace Corps, Alliance for Progress with Latin America, and the continuation of the Apollo program with the goal of landing a man on the Moon before 1970. He also supported the civil rights movement, but was only somewhat successful in passing his New Frontier domestic policies.

On November 22, 1963, he was assassinated in Dallas. Vice President Lyndon B. Johnson assumed the presidency upon Kennedy's death. Marxist and former U.S. Marine Lee Harvey Oswald was arrested for the state crime, but he was shot and killed by Jack Ruby two days later. The FBI and the Warren Commission both concluded Oswald had acted alone in the assassination, but various groups contested the Warren Report and believed that Kennedy was the victim of a conspiracy. After Kennedy's death, Congress enacted many of his proposals, including the Civil Rights Act and the Revenue Act of 1964. Despite his truncated presidency, Kennedy ranks highly in polls of U.S. presidents with historians and the general public. His personal life has also been the focus of considerable sustained interest following public revelations in the 1970s of his chronic health ailments and extramarital affairs. Kennedy was the most recent U.S. president to have been assassinated as well as the most recent U.S. president to die in office."""

DEFAULT_QUESTION = "What was the goal of the Apollo Program?"

navbar = dbc.Navbar(
    id="navbar",
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src=IMAGE_URL, height="70px",
                             style={"mixBlendMode": "multiply"})
                ),
                dbc.Col(
                    dbc.NavbarBrand(
                        "Natural Language Processing App",
                        style={
                            "fontSize": "35px",
                            "fontWeight": "500"
                        }
                    )
                )
            ],
            align="center",
            # no_gutters=True
        )
    ],
    style={
        "width": "100%"
    },
    color="primary"
)


app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    id="main",
    children=[
        html.Div(
            id="navContainer",
            children=[
                navbar
            ]
        ),
        html.Br(),
        html.H4("Context Paragraph"),
        html.Div(
            id="textContainer",
            children=[
                dcc.Textarea(
                    id="contextParagraph",
                    style={
                        "width": "60%",
                        "height": "90%"
                    },
                    value=DEFAULT_CONTEXT
                )
            ],
            style={
                "height": "45%",
                "width": "100%",
                "display": "grid",
                "placeItems": "center"
            }
        ),
        html.H4("Ask your question here"),
        html.Div(
            id="questionContainer",
            children=[
                dcc.Input(
                    id="questionInput",
                    style={
                        "width": "60%",
                        "height": "90%"
                    },
                    value=DEFAULT_QUESTION
                )
            ],
            style={
                "height": "5%",
                "width": "100%",
                "display": "grid",
                "placeItems": "center"
            }
        ),
        html.Div(
            id="buttonContainer",
            children=[
                dbc.Button(
                    id="submitButton",
                    type="submit",
                    children="Submit",
                    color="warning",
                    block=True,
                    n_clicks=0
                )
            ],
            style={
                "height": "8%",
                "width": "60%",
                "display": "grid",
                "placeItems": "center",
                "alignSelf": "center",
                "justifySelf": "center"
            }
        ),
        html.Div(
            id="answerContainer",
            children=[
                dcc.Loading(
                    id="loading",
                    type="default",
                    children=html.H3(id="answer")
                ),
            ],
            style={
                "height": "20%",
                "width": "100%",
                "display": "grid",
                "placeItems": "center"
            }
        )
    ],
    style={
        "height": "100vh",
        "width": "100vw",
        "display": "flex",
        "flexDirection": "column",
        "textAlign": "center",
    }
)

@app.callback(
    Output("answer", "children"),
    [
        Input("submitButton", "n_clicks")
    ],
    [
        State("contextParagraph", "value"),
        State("questionInput", "value")
    ]
)
def generateAnswer(clicks, context_provided, question_provided):
    if clicks > 0:
        nlp = pipeline("question-answering")
        return "Answer: " + nlp(question=question_provided, context=context_provided)["answer"]
    else:
        return ""



if __name__ == '__main__':
    app.run_server()
