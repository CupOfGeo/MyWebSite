import plotly.graph_objects as go
from plotly.subplots import make_subplots
#http://xahlee.info/SpecialPlaneCurves_dir/Seashell_dir/seashell_math_formulas.html
#By Xah Lee.
# Equation of ring cyclide
# see https://en.wikipedia.org/wiki/Dupin_cyclide
import numpy as np
import dash_html_components as html
import dash_bootstrap_components as dbc


#fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


u, v = np.mgrid[0:2*np.pi:100j, 0:2*np.pi:100j]

'''R=0.5    # radius of tube
N=4.6  # number of turns
H=2    # height
P=2    # power'''


R=.5    # radius of tube


def W(u):
    return (u/(2*np.pi)*R)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server
# app.title='SeaShells'

from app import app

layout = html.Div([
    html.H5("This equation is the work of Xah Lee and Mike Willams"),
    html.A("View the original work here!",href="http://xahlee.info/SpecialPlaneCurves_dir/Seashell_dir/seashell_math_formulas.html"),

    dcc.Graph(id='graph-shell'),
    html.P('wave frequency'),
    dcc.Slider(
        id='wave-freq-slider',
        min=50,
        max=100,
        value=80,
        step=10),
    html.P('number of turns'),
    dcc.Slider(
        id='turns-slider',
        min=1,
        max=6,
        value=4,
        step=.1),
    html.P('height'),
    dcc.Slider(
        id='height-slider',
        min=1,
        max=5,
        value=2,
        step=.5),
    html.P('power'),
    dcc.Slider(
        id='power-slider',
        min=.5,
        max=3,
        value=1.9,
        step=.1),
    html.P('wave amplitude'),
    dcc.Slider(
        id='wave-slider',
        min=0,
        max=1,
        value=.2,
        step=.1),

    dbc.Container([

        dbc.Row([
            dbc.Col(html.H5(children="They are made with 3 parametric equations that plot the shell a surface and a small function")
                    , className="mb-4"),
            ]),
        dbc.Row([
            dbc.Col(html.H5(['W(u) = (u/(2*pi)*R)',html.Br(),
                    'Fx = W(u)*cos(N*u)*(1+cos(v)+cos(F*u)*A)',html.Br(),
                    'Fy = W(u)*sin(N*u)*(1+cos(v)+cos(F*u)*A)', html.Br(),
                    'Fz = W(u)*sin(v) + H*(u/(2*pi))**P', html.Br()])
                    , className="mb-4"),

            ]),
    ]),


    html.Div(children='''
    This project was inspired by my love of shells and the beach. One of the
    running jokes of my comp sci career is that when people asked me what I want
    to do after college I would always respond. "I wanna sell sea shells by the
    seashore." I never found out what I wanna do at Bucknell but I did find what I love.
    That was learning math and science, building with computers and helping
    others how ever I can.
    ''')
    ])

@app.callback(
    Output('graph-shell', 'figure'),
    Input('wave-freq-slider', 'value'),
    Input('turns-slider', 'value'),
    Input('height-slider', 'value'),
    Input('wave-slider','value'),
    Input('power-slider','value'))

def update_figure(wave_freq,num_turns,height,wave_amp,pow):
    N=num_turns  # number of turns
    H=height  # height
    F=wave_freq   # wave frequency
    A=wave_amp  # wave amplitude
    P=pow  # power

    Fx = W(u)*np.cos(N*u)*(1+np.cos(v)+np.cos(F*u)*A)
    Fy = W(u)*np.sin(N*u)*(1+np.cos(v)+np.cos(F*u)*A)
    Fz = W(u)*np.sin(v) + H*(u/(2*np.pi))**P

    fig = make_subplots(rows=1, cols=1,
                        specs=[[{'is_3d': True}]],
                        subplot_titles=['Sea Shells Sea Shells by the Sea Shore'],
                        )

    fig.add_trace(go.Surface(x=Fx, y=Fy, z=Fz, colorbar_x=-0.07), 1, 1)
    #fig.add_trace(go.Surface(x=Fx, y=Fy, z=Fz, surfacecolor=x**2 + y**2 + z**2), 1, 2)
    fig.update_layout(title_text="Ring cyclide")
    #fig.show()

    fig.update_layout(transition_duration=500)

    return fig



#app.run_server(debug=True)
