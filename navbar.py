"""
A simple app demonstrating how to manually construct a navbar with a customised
layout using the Navbar component and the supporting Nav, NavItem, NavLink,
NavbarBrand, and NavbarToggler components.
Requires dash-bootstrap-components 0.3.0 or later
"""
import dash_core_components as dcc
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import server
from app import app
from apps import shells, attractors
import base64



#ME_LOGO = 'me.png' # replace with your own image
image_filename = 'me.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())




#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Sea Shells",href="/shell"),
        dbc.DropdownMenuItem("Lorenz Attractors",href="/lorenz"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Coming soon"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)



# this example that adds a logo to the navbar brand
logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [

                        dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height="50px")),
                        dbc.Col(dbc.NavbarBrand("George Mazzeo", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),

            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)


app.layout = html.Div([
    logo,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# we use a callback to toggle the collapse on small screens

@app.callback(
    Output(f"navbar-collapse2", "is_open"),
    [Input(f"navbar-toggler2", "n_clicks")],
    [State(f"navbar-collapse2", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# the same function (toggle_navbar_collapse) is used in all three callbacks




@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/shell':
        return shells.layout
    elif pathname == '/lorenz':
        return attractors.layout
    else:
        return shells.layout

if __name__ == "__main__":
    app.run_server(debug=True)
