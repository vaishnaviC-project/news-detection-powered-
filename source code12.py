import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

    st.subheader("1. Line Plot of True vs False Scores")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(y=df['True'], mode='lines', name='True', line=dict(color='green')))
    fig1.add_trace(go.Scatter(y=df['False'], mode='lines', name='False', line=dict(color='red')))
    st.plotly_chart(fig1)

    st.subheader("2. Box Plot of True and False Scores")
    fig2 = go.Figure()
    fig2.add_trace(go.Box(y=df['True'], name='True', marker_color='green'))
    fig2.add_trace(go.Box(y=df['False'], name='False', marker_color='red'))
    st.plotly_chart(fig2)

    st.subheader("3. Correlation Heatmap (True vs False)")
    corr_val = df[['True', 'False']].corr()
    fig3 = px.imshow(corr_val, text_auto=True, color_continuous_scale='RdBu')
    st.plotly_chart(fig3)

    st.subheader("4. Histogram of Margin (True - False)")
    fig4 = px.histogram(df, x='Margin', nbins=30, title='Margin Histogram', color_discrete_sequence=['purple'])
    st.plotly_chart(fig4)

    st.subheader("5. Distribution of True and False Scores")
    fig5 = go.Figure()
    fig5.add_trace(go.Histogram(x=df['True'], name='True', opacity=0.6, nbinsx=30, marker_color='green'))
    fig5.add_trace(go.Histogram(x=df['False'], name='False', opacity=0.6, nbinsx=30, marker_color='red'))
    fig5.update_layout(barmode='overlay')
    st.plotly_chart(fig5)

else:
    st.info("Please upload a CSV file to begin.")
