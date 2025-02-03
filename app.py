import streamlit as st
import pandas as pd
import plotly.express as px

# Function to Load Excel Data
@st.cache_data
def load_data():
    file_path = "military_inventory_final_with_quantity.xlsx"  # Ensure this file is in the same folder
    df = pd.read_excel(file_path)
    return df

# Streamlit Page Configuration
st.set_page_config(page_title="Waste Management Dashboard", layout="wide")

# Title and Header
st.title("♻️ Waste Management Dashboard")
st.markdown("Monitor and analyze waste data for better environmental impact.")

# Load Data
data = load_data()

# Show Raw Data (Expandable)
with st.expander("📂 View Raw Data"):
    st.dataframe(data)

# Summary Statistics
st.subheader("📊 Summary Statistics")
st.write(data.describe())

# Category Filter (if column exists)
if 'Category' in data.columns:
    category = st.selectbox("📌 Select Waste Category", options=data['Category'].unique())
    filtered_data = data[data['Category'] == category]
    st.write(filtered_data)

# Visualization: Waste by Category
if 'Category' in data.columns:
    st.subheader("📉 Waste Category Distribution")
    fig = px.bar(data, x='Category', y='Quantity', title="Waste by Category", color='Category')
    st.plotly_chart(fig)

# Visualization: Waste Trends Over Time
if 'Date' in data.columns:
    st.subheader("📈 Waste Trends Over Time")
    fig_trend = px.line(data, x='Date', y='Quantity', title="Waste Trends", color='Category')
    st.plotly_chart(fig_trend)

# Run this file with: `streamlit run app.py`
