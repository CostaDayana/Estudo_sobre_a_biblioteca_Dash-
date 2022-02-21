from turtle import color
from dash import Dash
from dash_html_components import Div, H1, P, H3
from dash_core_components import (
    Graph, Dropdown, Slider,
    Checklist, Interval
)
from dash.dependencies import Input, Output
from random import randint

external_stylesheets = [
    'https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css',
]

app = Dash(__name__, external_stylesheets=external_stylesheets)


N = 20

database = {
    'index': [],
    'maiores': [],
    'menores': [],
    'bebes': [],
}


app.layout = Div(children=[
        H1('Dashboard Interativo'),
        H3('idade das pessoas que foram ao evento'),
        Interval(id='interval'),
        Checklist(
            id='meu_check_list',
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value=['bebes']
        ),
        Dropdown(
            id='meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='line'
        ),
        Graph(
            id='meu_grafico',
            
        )
    ]
)


def update_database(value):
    """Minha query / Atualização do pandas."""
    database['index'].append(value)
    database['menores'].append(randint(1, 200))
    database['maiores'].append(randint(1, 200))
    database['bebes'].append(randint(1, 200))


@app.callback(
    Output('meu_grafico', 'figure'),
    [
        Input('meu_check_list', 'value'),
        Input('meu_dropdown', 'value'),
        Input('interval', 'n_intervals'),
    ]
)
def my_callback(input_data, graph_type, n_intervals):
    update_database(n_intervals)
    grafico = {
        'data': []
    }
    for x in input_data:
        grafico['data'].append(
            {
                'y': database[x][-20:],
                'x': database['index'][-20:],
                'name': x,
                'type': graph_type
            },
        )
    return grafico

app.run_server(debug=True)