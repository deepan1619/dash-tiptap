import dash_tiptap
import dash
from dash import html, Input, Output

app = dash.Dash(__name__)

mentions = [
    {'id': '1', 'label': 'Deepan S'},
    {'id': '2', 'label': 'Mithun V'},
    {'id': '3', 'label': 'Sheshathri VM'},
    {'id': '4', 'label': 'Ajeeth P'},
    {'id': '5', 'label': 'Gova N'},
    {'id': '6', 'label': 'Santhosh K'},
    {'id': '7', 'label': 'Rufus S'},
    {'id': '8', 'label': 'Hari P'},
    {'id': '9', 'label': 'Arun J'},
    {'id': '10', 'label': 'Vijay T'},
    {'id': '11', 'label': 'Dhanush K'},
]

app.layout = html.Div([
    html.H1("Dash Tiptap Mention Component Demo"),
    dash_tiptap.DashTiptap(
        id='input',
        value='<p>Hey!</p>',
        mentions=mentions
    ),
    html.H2("Output"),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return value

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050, debug=True)