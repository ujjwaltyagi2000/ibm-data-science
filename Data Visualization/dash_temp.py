# minimal test code for dash 

import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Hello Dash!"),
    # Add more components one by one
])

app.run_server(debug=True)
