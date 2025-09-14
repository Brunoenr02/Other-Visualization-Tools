import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data # Cache the data to improve performance
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
    df.dropna(inplace=True)
    return df

df = load_data()

# --- Page Configuration ---
st.set_page_config(
    page_title="🐧 Palmer Penguins Explorer",
    page_icon="🧊",
    layout="centered"
)

st.title("🐧 Palmer Penguins Explorer")
st.markdown("Explore the Palmer Penguins dataset using **Streamlit**.")

# --- Sidebar for User Inputs ---
st.sidebar.header("📊 Chart Controls")

# Species selector
species_list = ['All'] + sorted(df['species'].unique().tolist())
selected_species = st.sidebar.selectbox("Select Species", species_list)

# Axis selectors
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
x_axis = st.sidebar.selectbox("Select X-axis", numeric_columns, index=numeric_columns.index('bill_length_mm'))
y_axis = st.sidebar.selectbox("Select Y-axis", numeric_columns, index=numeric_columns.index('bill_depth_mm'))

# --- Data Filtering ---
if selected_species != 'All':
    filtered_df = df[df['species'] == selected_species]
else:
    filtered_df = df

# --- Display Chart ---
st.subheader(f"Scatter Plot: {x_axis} vs. {y_axis}")

if not filtered_df.empty:
    fig = px.scatter(
        filtered_df,
        x=x_axis,
        y=y_axis,
        color='species',
        hover_name='species',
        title=f'Relationship between {x_axis} and {y_axis}'
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data available for the selected species.")

st.markdown("---")
st.write("Data Source:")
st.dataframe(filtered_df.head())