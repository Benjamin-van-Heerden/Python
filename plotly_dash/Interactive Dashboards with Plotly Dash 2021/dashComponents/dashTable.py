import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd

df1 = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/multiple_y_axis.csv")

data = {
    'Date': ['July 12th, 2013 - July 25th, 2013', 'July 12th, 2013 - July 25th, 2013'],
    'Election Polling Organization': ['The New York Times', 'Pew Research'],
    'Rep': [10, 15],
    'Dem': [5, 20],
    'Region': ['Northern New York State to the Southern Appalachian Mountains', 'Canada']
}

df2 = pd.DataFrame(data)


app = dash.Dash()

table1 = dash_table.DataTable(
    data=df1.to_dict("records"),
    columns=[{"id": c, "name": c} for c in df1.columns],
    fixed_rows={"headers": True},
    style_table={
        "maxHeight": "450px"
    },
    style_header={
        "backgroundColor": "black",
        "fontweight": "800",
        "border": "3px solid black",
        "fontSize": "20px"
    },
    style_data_conditional=[
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "lightgrey",
            "fontSize": "15px"
        },
        {
            "if": {"row_index": "even"},
            "backgroundColor": "white",
            "fontSize": "15px"
        }
    ],
    style_cell={
        "textAlign": "center",
        "border": "2px solid white"
    }
)

table2 = dash_table.DataTable(
    data=df2.to_dict("records"),
    columns=[{"id": c, "name": c} for c in df2.columns],
    fixed_rows={"headers": True},
    style_table={
        "maxHeight": "450px"
    },
    style_header={
        "backgroundColor": "lightblue",
        "fontweight": "800",
        "border": "3px solid black",
        "fontSize": "20px"
    },
    style_data_conditional=[
        {
            "if": {"row_index": "odd"},
            "backgroundColor": "lightgrey",
            "fontSize": "15px"
        },
        {
            "if": {"row_index": "even"},
            "backgroundColor": "white",
            "fontSize": "15px"
        }
    ],
    style_cell={
        "textAlign": "center",
        "border": "2px solid white",
        "maxWidth": "50px",
        "whiteSpace": "normal"
    }
)


app.layout = html.Div(
    id="main",
    children=[
        table1,
        html.Br(),
        table2
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
