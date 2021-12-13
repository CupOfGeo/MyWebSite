#import datetime
import numpy as np
from PIL import Image

import dash
import requests
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import json
from app import app



#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    dbc.Row([
        dbc.Col(html.H3('Style Transfer frontend changes coming soon')
                , className="mb-4")
    ]),

    html.Div(id='output_title'),
    html.Img(id='output'),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='content-image-upload'),
dcc.Upload(
        id='upload-image-style',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='style-image-upload'),
    dbc.Button(
        id='button',
        children='Submit'
    ),

    # dbc.Row([
    #         dbc.Col(html.H5('This is the first ml model I have ever deployed on the internet for people to use.'
    #                         'No this is not my model this is actually 2 models from tensorflow lite.'),
    #                 html.A("Here's the Link to the original notebook on github",href='https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/examples/style_transfer/overview.ipynb'),
    #                 html.H5("They are two very small models together only about 5MB and are rather quick and can be done on a processor. "
    #                         "Perfect for deploying on a serverless node. Sounds nice but it comes with some tradeoffs of quality."
    #                         "I have built my own neural style transfer from the VGG19 model which is a large pretrained convolution image classification network."
    #                         #It was trained on the ImageNet dataset which has over 1.4 million images in total.
    #                         # It can do 1000 different class classifications
    #                         "It has 19 layers of convolutions hence the name and is over 100X larger at around 625MB."
    #                         "How it works is the neurel network learned some filters while training. It also learns what pictures it should apply which filters too. So it doenst use all of the filters."
    #                         " Of the filters it thinks it should you we take a sort of average of them to attempt to understand the 'style' of the images.")
    #
    #
    #                 , className="mb-4")
    #     ]),




    # html.Div(children='''
    # This is a Neural style transfer here is the orginal paper https://arxiv.org/abs/1508.06576.
    #
    # This uses the VGG19 model which is a large pretrained convolution image classification network.
    # It was trained on the ImageNet dataset which has over 1.4 million images in total.
    # It can do 1000 different class classifications
    # mostly animals but here's a list (https://image-net.org/challenges/LSVRC/2014/browse-synsets).
    # ''')
])


def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        #html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents),
        html.Hr(),
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    ])


@app.callback(Output('content-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


@app.callback(Output('style-image-upload', 'children'),
              Input('upload-image-style', 'contents'),
              State('upload-image-style', 'filename'),
              State('upload-image-style', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


def clean_filename(style_name, content_name):
    style_name = style_name[:style_name.find('.')]
    content_name = content_name[:content_name.find('.')]
    style_name = style_name.replace(' ','_')
    content_name = content_name.replace(' ', '_')
    cleaned = content_name + '_' +  style_name
    return cleaned

@app.callback(Output('output', 'src'),
            Output('output_title', 'children'),
            Input('button','n_clicks'),
            State('upload-image-style', 'contents'),
            State('upload-image-style', 'filename'),
            State('upload-image', 'contents'),
            State('upload-image', 'filename'))
def submit_button(clk, style,style_name, content, content_name):
    #put them into json
    data = {}

    data['style'] = style
    data['content'] = content


    # f = open('JSON_TEST.txt', 'w')
    # f.write(json.dumps(data))
    # f.close()
    url = 'https://us-central1-atrractors.cloudfunctions.net/function-2'
    res = requests.post(url, json=data)
    print(res.status_code)
    #print(res.json())
    json_data = res.json()['out']

    #new_image
    #new_image.save('output.png')
    if type(res.json()['out']) == type('string'):
        return '', ''
    else:
        clean_name = clean_filename(style_name[0], content_name[0])
        new_image = Image.fromarray(np.array(json_data, dtype='uint8'))
        return new_image, clean_name
