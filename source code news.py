import streamlit as st
import pandas as pd


# Streamlit app title
st.title("Truthfulness Data Visualizations")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Load CSV
    df = pd.read_csv(uploaded_file)

    # Preprocess data
    df['True'] = pd.to_numeric(df['True'], errors='coerce')
    df['False'] = pd.to_numeric(df['False'], errors='coerce')
    df = df.dropna(subset=['True', 'False'])
    df['Margin'] = df['True'] - df['False']

    