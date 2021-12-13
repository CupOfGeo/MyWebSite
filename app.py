import dash
import dash_bootstrap_components as dbc
#[dbc.themes.LUX] #DARKLY
#[dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])
server = app.server
app.title='CupOfGeo'
