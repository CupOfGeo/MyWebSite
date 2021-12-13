import plotly.graph_objects as go
from plotly.subplots import make_subplots
#http://xahlee.info/SpecialPlaneCurves_dir/Seashell_dir/seashell_math_formulas.html
import plotly.express as px
import pandas as pd

import numpy as np

import dash

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app


#app.config.suppress_callback_exceptions = True
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout = html.Div([
    html.Div(children='''
    Lorenz Attractors equation writen by no other than Edward Norton Lorenz
    https://en.wikipedia.org/wiki/Lorenz_system

    dx/dt = s*(y - x)
    dy/dt = r*x - y - x*z
    dz/dt = x*y - b*z

    these three differentiable equation that when given the right values of s,r, and b
    can give rise to chaotic behavior. Give it a try!
    '''),
    dcc.Graph(id='graph-lorenz'),#,style={'width': '80vh', 'height': '80vh'}),
    html.P('S'),
    dcc.Slider(
        id='S-slider',
        min=0,
        max=100,
        value=10,
        step=1),
    html.P('R'),
    dcc.Slider(
        id='R-slider',
        min=0,
        max=100,
        value=28,
        step=1),
    html.P('B'),
    dcc.Slider(
        id='B-slider',
        min=1,
        max=5,
        value=2.667,
        step=.001),

    html.Div(children='''
    This project was inspired by my love of information theory, chaos theory and
    complex systems. This was actually my favorite lab from numerical analysis
    but this time in 3d!
    ''')
])



@app.callback(
    Output('graph-lorenz', 'figure'),
    [Input('S-slider', 'value'),
    Input('R-slider', 'value'),
    Input('B-slider', 'value')])
def update_figure(S,R,B):
    def lorenz(x, y, z, s=S,r=R,b=B):#s=10, r=28, b=2.667):
    # """
    # Given:
    #    x, y, z: a point of interest in three dimensional space
    #    s, r, b: parameters defining the lorenz attractor
    # Returns:
    #    x_dot, y_dot, z_dot: values of the lorenz attractor's partial
    #        derivatives at the point x, y, z
    # """
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot


    dt = 0.001
    num_steps = 10000

    # Need one more for the initial values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Set initial values
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Step through "time", calculating the partial derivatives at the current point
    # and using them to estimate the next point
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)
    df = pd.DataFrame({'x':xs,'y':ys,'z':zs})
    fig = px.line_3d(df, x="x", y="y", z="z")


    return fig



#app.run_server(debug=True)
