import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
import time
from app import app



#app = dash.Dash(__name__, suppress_callback_exceptions=True)

print('App is starting..')

layout = html.Div([
	html.H3("Rick And Morty Generator comming soon",
			style={
				   'text-align': 'center',}
			),
html.H5(children=["Hello this page will one day be where you can generate your own rick and morty transcript."
		"I will also like to add my rick voice model heres a small sample",],
			style={
				   'text-align': 'center',}
			),
html.Audio(src='assets/rick_voice.wav',controls=True),

    html.Div(
            [
                dcc.Textarea(id="loading-input-2",
							 draggable='false', rows="5",
							 value='Input triggers nested spinner',
							 style={'resize': 'none', 'width':'80%',
									'display': 'block',
									'margin-left': 'auto',
    								'margin-right': 'auto'}),
                dcc.Loading(
                    id="loading-2",
                    children=[html.Div([html.Div(id="loading-output-2")])],
                    type="circle",
                )
            ]),
    html.Div(id='dynamic-button-container',
    	children=[
    	html.Button(
    		#id={'type': 'dynamic-button', 'index': 0 },
    		id = 'button0',
    		children= 'Submit'
    		)
    	]),


])

@app.callback(
    Output('dynamic-button-container', 'children'),
    Output("loading-output-2", "children"),
    [#Input({'type': 'dynamic-button', 'index': ALL}, 'n_clicks')
    Input('button0', 'n_clicks')
    ],
    [State('dynamic-button-container', 'children'),
     State("loading-input-2",'value')])
def display_newbutton(n_clicks, children, input):
	#if n_clicks[0] is None: return children
	if n_clicks is None: return children, input
	else:
		print('Doing some calculation..')
		time.sleep(3)

		new_element = html.Button(
		        #id={'type': 'dynamic-button','index': 0 }, #n_clicks[0] },
		        id = 'button0',
		        children = 'Button'
		    	)

		children.pop()
		children.append(new_element)
		print('Generating a new button')
		return children, ''

# @app.callback(
#     Output({'type': 'dynamic-button', 'index': 0}, 'disabled'),
#     [Input({'type': 'dynamic-button', 'index': 0}, 'n_clicks')]
# )
@app.callback(
    Output('button0', 'disabled'),
    [Input('button0', 'n_clicks')]
)
def hide_newbutton(n_clicks):
	if n_clicks is None: return False
	else:
		print('Disabling the button')
		return True



# @app.callback(Output("loading-output-2", "children"), Input("loading-input-2", "value"))
# def input_triggers_nested(value):
#     time.sleep(1)
#     print('value:',value)
#     return value


