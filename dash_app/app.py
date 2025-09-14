import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
df.dropna(inplace=True)

# --- App Initialization ---
app = dash.Dash(__name__)
server = app.server # Expose server for deployment

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
species_list = [{'label': 'All', 'value': 'All'}] + [{'label': s, 'value': s} for s in sorted(df['species'].unique())]

# --- App Layout ---
app.layout = html.Div(style={'fontFamily': 'sans-serif'}, children=[
    html.H1("🐧 Palmer Penguins Explorer (Dash)", style={'textAlign': 'center'}),
    html.P("Explore the Palmer Penguins dataset using Plotly Dash.", style={'textAlign': 'center'}),
    
    html.Div(style={'display': 'flex', 'padding': '20px'}, children=[
        # Controls Div
        html.Div(style={'width': '25%', 'paddingRight': '20px'}, children=[
            html.H3("📊 Chart Controls"),
            html.Label("Select Species"),
            dcc.Dropdown(id='species-dropdown', options=species_list, value='All'),
            html.Br(),
            html.Label("Select X-axis"),
            dcc.Dropdown(id='x-axis-dropdown', options=[{'label': i, 'value': i} for i in numeric_columns], value='bill_length_mm'),
            html.Br(),
            html.Label("Select Y-axis"),
            dcc.Dropdown(id='y-axis-dropdown', options=[{'label': i, 'value': i} for i in numeric_columns], value='bill_depth_mm'),
        ]),
        
        # Graph Div
        html.Div(style={'width': '75%'}, children=[
            dcc.Graph(id='penguin-scatter-plot')
        ])
    ])
])

# --- Callback for Interactivity ---
@app.callback(
    Output('penguin-scatter-plot', 'figure'),
    [Input('species-dropdown', 'value'),
     Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value')]
)
def update_graph(selected_species, x_axis, y_axis):
    if selected_species == 'All' or selected_species is None:
        filtered_df = df
    else:
        filtered_df = df[df['species'] == selected_species]
        
    fig = px.scatter(
        filtered_df,
        x=x_axis,
        y=y_axis,
        color='species',
        hover_name='species',
        title=f'Relationship between {x_axis} and {y_axis}'
    )
    fig.update_layout(transition_duration=500)
    return fig

# --- Run the App ---
if __name__ == '__main__':
    app.run_server(debug=True)