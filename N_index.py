import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import server
from app import app
from apps import shells
from apps import attractors


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/shells':
        return shells.layout
    elif pathname == '/lorenz':
        return attractors.layout
    else:
        return shells.layout

if __name__ == '__main__':
    app.run_server(debug=True)
