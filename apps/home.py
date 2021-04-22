import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead

# needed only if running this as a single page app
# if __name__ == '__main__':
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to George Mazzeo's Gallery", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children="Welcome friends family and possible future friends. I'm having a great time in Chicago right now all is good! I hope you enjoy my work")
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='This app is a gallery of interactive projects and art I want to share with the world.'
                                     '')
                    , className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Get the original datasets used in this dashboard',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Lorenz Attractors", href="/lorenz",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                dbc.Col(dbc.Button("More Attractors", href="/attractors",
                                                                   color="primary"),
                                                        className="mt-3")
                                                ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this site and apps are on my Github',
                                               className="text-center"),
                                       dbc.Button("CupOfGeo",
                                                  href="https://github.com/CupOfGeo",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Sea Shells',
                                               className="text-center"),
                                       dbc.Button("Sea Shells",
                                                  href="/shell",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5"),

        # html.A("Special thanks to Flaticon for the icon in COVID-19 Dash's logo.",
        #        href="https://www.flaticon.com/free-icon/coronavirus_2913604")

        dbc.Row([
            dbc.Col(html.H5(
                children="Who am I?")
                    , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H5(
                children=["Hello I am George.",html.Br(),
                         " Im a python Developer who loves learning and building. I love giving people the opportunity "
                         "to interact with the math and code themselves so they can have a better intuition about whats "
                         "actually happening other than just looking and some words or plots. Currently Im very focused "
                         "on ML/AI and data science. I find a lot of beauty in chaos and information theory so I like all"
                         " kinds of data."])
                , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H5(
                children=["Who do I want to become?",html.Br(),"    I want to become someone who can really help make the world a better place for all of us earthlings"]
            )
                , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(
                children=["Currently reading: Genius Makers by Cade Metz" ,html.Br(),
                         "reading list:" ,html.Br(),
                         "Atomic Habit by James Clear",html.Br(),
                         "Genius: The Life and Science of Richard Feynman by James Gleick",html.Br(),
                         "Ultralearning Scott Young" ,html.Br(),
                         "Humankind: A hopeful History",html.Br(),]

            )
                , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(
                children=["Books I read:",html.Br(),
"Surely You're Joking, Mr. Feynman!",html.Br(),
'Sapiens',html.Br(),
'Outliers',html.Br(),
'The grand design ',html.Br(),
'Nine pints by Rose George',html.Br(),
'The 7 habits of highly effective people ',html.Br(),
'chaos by james gleick',html.Br(),
'Influence Science and Practice by Robert Cialdini',html.Br(),
'QED by Feynman',html.Br(),
'What do you care what other people think by Feynman',html.Br(),
'Astrophysics for people in a hurry by Tyson',html.Br(),
'Talking to stranger by Gladwell',html.Br(),
'Red Notice by Bill Browder',html.Br(),
'The Code Book by Simon Singh',html.Br(),
'Everybody Lies by Seth Stephens-Davidowitz',html.Br(),
'Naked Statistics by Charles Wheelan',html.Br(),
'Range by David Epstine',html.Br(),
'the Signal and the Noise by Nate Silver',html.Br(),
'The Physics of Wall street James Owen Weatherall',html.Br(),
'David and Goliath Malcum',html.Br(),
'Programming the Universe Seth Lloyd',html.Br(),
"Lost in Math Sabine Hossenfelder",html.Br(),]
            )
                , className="mb-4")
        ]),



    ])

])
#     app.run_server(host='127.0.0.1', debug=True)