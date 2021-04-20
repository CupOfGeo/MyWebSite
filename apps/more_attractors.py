import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
from PIL import Image
import pandas as pd
import json
import requests
#import resource
from app import app
from cliff_attractor import gen_random, make_pretty, make_detailed

big_cmaps = ['CET_C5',
 'CET_C1s',
 'CET_C2',
 'colorwheel',
 'CET_CBC1',
 'CET_CBC2',
 'CET_CBTC1',
 'CET_CBTC2',
 'CET_C4',
 'CET_C4s',
 'bkr',
 'bky',
 'CET_D13',
 'CET_D1A',
 'coolwarm',
 'CET_D9',
 'CET_D10',
 'diverging_gkr_60_10_c40',
 'CET_D3',
 'gwv',
 'CET_D12',
 'diverging_isoluminant_cjm_75_c24',
 'CET_D11',
 'CET_D8',
 'bjy',
 'bwy',
 'CET_R3',
 'cwr',
 'CET_I1',
 'isolum',
 'CET_I3',
 'bgy',
 'linear_bgyw_15_100_c67',
 'bgyw',
 'CET_L9',
 'kbc',
 'blues',
 'CET_L7',
 'bmw',
 'CET_L8',
 'bmy',
 'CET_L10',
 'CET_L11',
 'kgy',
 'gray',
 'dimgray',
 'CET_L16',
 'kgy',
 'CET_L4',
 'linear_kry_5_95_c72',
 'linear_kry_5_98_c75',
 'fire',
 'linear_kryw_5_100_c64',
 'linear_kryw_5_100_c67',
 'CET_CBL1',
 'CET_CBL2',
 'kb',
 'kg',
 'kr',
 'CET_CBTL2',
 'CET_CBTL1',
 'CET_L19',
 'CET_L17',
 'CET_L18',
 'CET_R2',
 'rainbow',
 'CET_R1',
 'rainbow_bgyrm_35_85_c71']





layout = html.Div([
    #,style={'width': '80vh', 'height': '80vh'}),
    html.Div(children='''
    Welcome, please wait for your attractor to generate before clicking the
    button or dropdown if one doesnt generate in 30 second you may try clicking
    the button this page is a work in progress!

    The base code is from Lázaro Alonso
    https://lazarusa.github.io/Webpage/index.html
    I didnt see any place for less technical people to generate and
    color there own attractors and wanted to share with my sisters and friends 
    '''),
    html.Img(id='frac'),
    html.Button('New Attractor', id='submit-val', n_clicks=0),
    dcc.Dropdown(
        id='color-dropdown',
        options=[{'label':x, 'value':x} for x in big_cmaps],
        value='rainbow'
    ),


    html.Div(id='inital-params',children='',style={'display': 'none'}),
    html.Div(id='agg-params',children='',style={'display': 'none'}),
    html.Div(children='''
    This program uses the Clifford formula
    x = sin(a * y) + c * np.cos(a * x)
    y = np.sin(b * x) + d * np.cos(b * y)

    fractles work by you starting with some inital conditions
    I start with x[0] and y[0] = 0
    and 4 other parameters a,b,c, and d.

    then with the intial conditions and the other 4 paraments they are put into
    this equation and then you get a new value for x and y and then you take
    your new result and feed that again into the Clifford equation. the fracles
    you see here are run throught this equation 100,000,000 times.

    I set these with random numbers and then do a little bit of extra math find
    paramets that generate what i think are more intresting/pretty fracels. I also
    do some fancy math to compute them more effecently as they are easy and
    quick to calculate but become very spacous and quick very fast. So i had to
    move the computation off heroku who im using to host this site and trn it
    into a google cloud function api call where i can give it a little more ram.

    I want people to be able to generate and color there own fracles and admire
    there beauty as i do with every one.


    '''),
])

@app.callback(
    [Output('inital-params', 'children'),Output('agg-params', 'children')],
    [Input('submit-val', 'n_clicks')])
def new_frac(value):
    #x = requests.get('https://us-central1-atrractors.cloudfunctions.net/function-1?message=0')
    #agg = eval(x.text)

    vals = gen_random()

    #agg = make_detailed(vals)
    str_vals = str(vals[:])[1:-1].replace(', ','#')
    x = requests.get('https://us-central1-atrractors.cloudfunctions.net/function-1?message='+str_vals)
    print(str_vals)
    agg = eval(x.text)


    return vals, json.dumps(agg)

@app.callback(
    Output('frac', 'src'),
    [Input('color-dropdown', 'value'),
    Input('inital-params', 'children'),
    Input('agg-params', 'children')])
def color_figure(color, vals, agg):
    agg = eval(agg)
    out = make_pretty(color, vals, agg).to_pil()
    return out
