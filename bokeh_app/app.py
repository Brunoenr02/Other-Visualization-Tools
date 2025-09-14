import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column, row
from bokeh.palettes import Category10_3

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
df.dropna(inplace=True)

# Map species to colors
species_unique = sorted(df['species'].unique())
color_map = {species: Category10_3[i] for i, species in enumerate(species_unique)}
df['color'] = df['species'].map(color_map)

# Create a ColumnDataSource
source = ColumnDataSource(data=df)

# --- Create Widgets ---
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
species_list = ['All'] + species_unique

x_axis_select = Select(title="Select X-axis", value="bill_length_mm", options=numeric_columns)
y_axis_select = Select(title="Select Y-axis", value="bill_depth_mm", options=numeric_columns)
species_select = Select(title="Select Species", value="All", options=species_list)

# --- Create the Plot ---
p = figure(height=500, width=700, title="Penguin Scatter Plot", tooltips=[("Species", "@species"), ("X", "@x"), ("Y", "@y")])
p.circle(x="x", y="y", source=source, size=10, color="color", legend_field="species")
p.xaxis.axis_label = x_axis_select.value
p.yaxis.axis_label = y_axis_select.value

# --- Define the Callback ---
def update_plot(attr, old, new):
    # Filter data based on species selection
    if species_select.value == 'All':
        filtered_df = df
    else:
        filtered_df = df[df.species == species_select.value]
    
    # Update source data
    source.data = {
        'x': filtered_df[x_axis_select.value],
        'y': filtered_df[y_axis_select.value],
        'species': filtered_df['species'],
        'color': filtered_df['color']
    }
    
    # Update axis labels
    p.xaxis.axis_label = x_axis_select.value
    p.yaxis.axis_label = y_axis_select.value

# Attach the callback to the 'value' property of each widget
for widget in [x_axis_select, y_axis_select, species_select]:
    widget.on_change('value', update_plot)

# --- Arrange Layout ---
controls = column(species_select, x_axis_select, y_axis_select, width=200)
layout = row(controls, p)

# Initialize the plot data
update_plot(None, None, None) 

curdoc().add_root(layout)
curdoc().title = "🐧 Palmer Penguins Explorer (Bokeh)"