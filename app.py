from dash import Dash, html, dcc, Input, State
import pandas as pd


df = pd.DataFrame({
    "Tasks": ["Groceries", "Take kid from school", "GO to work", "Learn dash", "Breathe"],
    "Label": ["Home", "Familly", "Business", "Hobby", "Self-care"],
    "Status": ["Open", "Closed", "Closed", "Active", "Open"]
})



def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H2(children='To-do list'),

    html.Div(children=[
        html.Label('Task'),
        dcc.Dropdown(df['Tasks'], id = 'dropdown-task'),

        html.Br(),
        html.Label('Status', id = 'dropdown-status'),
        dcc.Dropdown(df['Status'].unique()),
        html.Br(),
        html.Button('Submit', id='submit-val', n_clicks=0)

    ], style={'padding': 10, 'flex': 1}),




    generate_table(df)
])

@app.callback(
    Input('submit-val', 'n_clicks'),
    Input('dropdown-status', 'value_status'),
    Input('dropdown-task', 'value_task')
)
def update_output(n_clicks, value_status, value_task):
    df.loc[df["Tasks"] == value_task, "Tasks"] = value_status
    



if __name__ == '__main__':
    app.run_server(debug=True)