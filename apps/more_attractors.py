import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
from PIL import Image
import pandas as pd
from app import app

from cliff_attractor import gen_random, make_pretty

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



#app = dash.Dash(__name__)

#app.
layout = html.Div([
    #,style={'width': '80vh', 'height': '80vh'}),
    html.Img(id='frac'),
    dcc.Dropdown(
        id='color-dropdown',

        options=[{'label':x, 'value':x} for x in big_cmaps],
        value='rainbow'
    ),

    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='inital-params',children='',style={'display': 'none'}),
    html.Div(id='agg-params',children='',style={'display': 'none'})

    # html.P('S'),
    # dcc.Slider(
    #     id='S-slider',
    #     min=150000,
    #     max=250000,
    #     value=240000,
    #     marks={
    #     150000: '150 Min',
    #     175000: '175',
    #     200000: '200 Mid',
    #     225000: '225',
    #     250000: '250 Max'
    # },)
])

@app.callback(
    [Output('inital-params', 'children'),Output('agg-params', 'children')],
    [Input('submit-val', 'n_clicks')])
def update_output(value):
    vals, df = gen_random()
    print('input:', value)

    return vals, df.to_json(date_format='iso', orient='split')


@app.callback(
    Output('frac', 'src'),
    [Input('color-dropdown', 'value'),
    Input('inital-params', 'children'),
    Input('agg-params', 'children')])
def update_figure(color, vals, df):
    print(color)
    df = pd.read_json(df, orient='split')
    if vals != '':
        im, a, df = make_pretty(color,vals, df)
        im = im.to_pil()
        return im
    else:
        return
    #im.save('im.png')
    #plot(func, vals=[["kbc"]+list(rvals[i]) for i in range(len(rvals))], label=True) #NOTEBOOK TO FILE

    # color_map = palette['inferno']
    # img = tf.shade(a,cmap=color_map).to_pil()
    # img.save('img.png')

    return fig




# if __name__ == "__main__":
#     app.run_server(debug=True)
