import plotly.graph_objects as go
from plotly.subplots import make_subplots
#http://xahlee.info/SpecialPlaneCurves_dir/Seashell_dir/seashell_math_formulas.html

# Equation of ring cyclide
# see https://en.wikipedia.org/wiki/Dupin_cyclide
import numpy as np
import dash_html_components as html


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


'''Fx = W(u)*np.cos(N*u)*(1+np.cos(v))
Fy = W(u)*np.sin(N*u)*(1+np.cos(v))
Fz = W(u)*np.sin(v) + H*(u/(2*np.pi))**P
'''



app = dash.Dash()

app.layout = html.Div([
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
    html.P('wave amplitude'),
    dcc.Slider(
        id='wave-slider',
        min=0,
        max=1,
        value=.2,
        step=.1)
    ])

@app.callback(
    Output('graph-shell', 'figure'),
    Input('wave-freq-slider', 'value'),
    Input('turns-slider', 'value'),
    Input('height-slider', 'value'),
    Input('wave-slider','value'))

def update_figure(wave_freq,num_turns,height,wave_amp):
    N=num_turns  # number of turns
    H=height  # height
    F=wave_freq   # wave frequency
    A=wave_amp  # wave amplitude
    P=1.9  # power

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



app.run_server(debug=True, use_reloader=False,port=8052)
