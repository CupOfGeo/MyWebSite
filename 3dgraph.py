import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)






app.layout = html.Div(
    [
    #style={'width': '90vh', 'height': '90vh'},
        dcc.Graph(id='graph', figure={'layout': {'height': 700,'width': 1000,}}),
        

        #html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
        html.Br(),
        html.Div(id="output"),
        dcc.Input(id="input1", type="text", value='(h-u)/h * r * sin(v)', debounce=True),
        dcc.Input(id="input2", type="text", value='(h-u)/h * r * cos(v)', debounce=True),
        dcc.Input(id="input3", type="text", value='v', debounce=True),

    ]
)


@app.callback(Output("output", "children"),
Input("input1", "value"),
Input("input2", "value"),
Input("input3", "value"))
def update_eq(input1, input2, input3):
    return u'x = {}, y = {}, z = {}'.format(input1, input2, input3)


def parse_input(eq):
    py_keywords = ['=', 'False','break','for','not','None','class','from','or','True','continue',
    'global','pass', '__peg_parser__', 'def', 'if','raise','and','del','import',
    'return','as','elif',' in ','try','assert','else','is','while','async',
    'except','lambda','with','await','finally','nonlocal','yield']
    for key in py_keywords:
        if key in eq:
            return 'error '+ key + eq

    numpy_convert = ['cos','sin','tan','pi']
    for s in numpy_convert:
        if s in eq:
            eq = eq.replace(s,'np.'+s)
    return str(eq)


@app.callback(
    Output('graph', 'figure'),
    Input("input1", "value"),
    Input("input2", "value"),
    Input("input3", "value"),
)
def update_figure(in_x, in_y, in_z):

    h = 3
    r = .8
    u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j] #TODO button to go from parametric to linear

    y = eval(parse_input(in_y))
    z = eval(parse_input(in_z))

    #x, y = np.mgrid[-1:1:100j, -1:1:100j]

    try:
        x = eval(parse_input(in_x)) #x=(h-u)/h * r * np.cos(v)#(c+a*np.cos(v))*np.cos(u) torus
    except NameError as e:# name 'h' is not defined
        print(e)
    except:
        print('ERROR IN X')

    try:
        y = eval(parse_input(in_y)) #y=(h-u)/h * r * np.sin(v)#(c+a*np.cos(v))*np.sin(u)
    except NameError as e:# name 'h' is not defined
        print(str(e).split(' ')[1][1:-1])
    except:
        print('ERROR IN Y')

    try:
        z = eval(parse_input(in_z))#z=u#(c+a*np.cos(v))*np.sin(u)
    except NameError as e:# name 'h' is not defined
        print(e)
    except:
        print('ERROR IN Z')

    #x = u
    #y = v
    #k=3.0
    #z = x**2 - y**2
    #x=(h-u)/h * r * np.cos(v)#(c+a*np.cos(v))*np.cos(u) torus
    #y=(h-u)/h * r * np.sin(v)#(c+a*np.cos(v))*np.sin(u)
    #z=u#a*np.sin(v)



    # fig = make_subplots(rows=1, cols=1,
    #                     specs=[[{'is_3d': True}]],
    #                     subplot_titles=['Color corresponds to z', 'Color corresponds to distance to origin'],
    #                     )
    try:
        fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorbar_y=-0.07)])
    except:
        fig = go.Figure()
    #fig.add_trace(go.Surface(x=x, y=y, z=z, surfacecolor=x**2 + y**2 + z**2), 1, 2)
    fig.update_layout(title_text="distance from z=0",)#width=700, height=700, autoexpand=True)) margin=dict(l=65, r=50, b=65, t=90,)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
