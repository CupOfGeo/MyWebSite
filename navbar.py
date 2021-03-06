"""
A simple app demonstrating how to manually construct a navbar with a customised
layout using the Navbar component and the supporting Nav, NavItem, NavLink,
NavbarBrand, and NavbarToggler components.
Requires dash-bootstrap-components 0.3.0 or later
"""
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from dash.dependencies import Input, Output, State
from app import server
from app import app
from apps import shells, attractors, more_attractors, home, style_transfer, rick_gen
import base64



image_filename = 'me.png' # logo
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
#'data:image/png;base64,{}'.format(encoded_image.decode())



#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Home", href="/home"))

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Sea Shells",href="/shell"),
        dbc.DropdownMenuItem("Lorenz Attractors",href="/lorenz"),
        dbc.DropdownMenuItem("More Attractors",href="/attractors"),
        dbc.DropdownMenuItem("Style Transfer",href="/style_transfer"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Coming soon"),
        dbc.DropdownMenuItem("Rick & Morty Generator",href='/rick_gen'),
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
                    className="g-0"
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
    elif pathname == '/attractors':
        return more_attractors.layout
    elif pathname == '/style_transfer':
        return style_transfer.layout
    elif pathname == '/rick_gen':
        return rick_gen.layout
    else:
        return home.layout

if __name__ == "__main__":
    app.run_server(debug=True)
