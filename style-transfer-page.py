import datetime

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from os import listdir
import base64



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '80%',
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
    html.Div(id='output-image-upload'),



])


# def parse_contents(contents, filename, date):
#     file1 = open('style_transfer_images/' + filename.split('.')[0],'w+')
#     file1.write(contents)
#     file1.close()
#     return html.Div([
#         html.H5(filename),
#         html.H6(datetime.datetime.fromtimestamp(date)),
#
#         # HTML images accept base64 encoded strings in the same format
#         # that is supplied by the upload
#         html.Img(src='data:image/png;base64,{}'.format(encoded_image), width=300, height=300),
#         html.Hr(),
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'

#
#     ])


@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'),
              State('output-image-upload', 'children'))
def update_output(list_of_contents, list_of_names, list_of_dates, prev_images):
    #save content to style_transfer_images/filename

    files = [f for f in listdir('style_transfer_images')]
    print(files)
    list_of_elements = []
    for file in files:
        encoded_image = base64.b64encode(open('style_transfer_images/'+file, 'rb').read())
        list_of_elements.append(html.H5(file))
        list_of_elements.append(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
            style={'display': 'block',
            'margin-left': 'auto',
            'margin-right': 'auto',}))

    children = html.Div(list_of_elements)
    return children


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')