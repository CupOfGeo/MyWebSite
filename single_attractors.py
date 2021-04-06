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

from cliff_attractor import gen_random, make_pretty, make_detailed

big_cmaps = ['CET_C5',
 'CET_C5s',
 'CET_C1',
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
 'Diverging_isoluminant_cjm_75_c24',
 'CET_D11',
 'CET_D8',
 'bjy',
 'bwy',
 'CET_R3',
 'cwr',
 'glasbey_bw',
 'glasbey',
 'glasbey_cool',
 'glasbey_warm',
 'glasbey_dark',
 'glasbey_light',
 'glasbey_category10',
 'glasbey_hv',
 'CET_I1',
 'isolum',
 'CET_I3',
 'bgy',
 'Linear_bgyw_15_100_c67',
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
 'kbc',
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



app = dash.Dash(__name__)

app.layout = html.Div([
    #,style={'width': '80vh', 'height': '80vh'}),
    html.Img(id='frac'),
    html.Button('New Attractor', id='submit-val', n_clicks=0),
    dcc.Dropdown(
        id='color-dropdown',
        options=[{'label':x, 'value':x} for x in big_cmaps],
        value='rainbow'
    ),


    html.Div(id='inital-params',children='',style={'display': 'none'}),
    html.Div(id='agg-params',children='',style={'display': 'none'})

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





if __name__ == "__main__":
    app.run_server(debug=True)
