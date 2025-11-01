import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("👑 Loyalty & Preferences Analysis")
st.markdown("This section explores the influence of **Product Preferences** and **Customer Loyalty** on purchase behavior.")

# --- Configuration and Data Loading ---

@st.cache_data
def load_and_process_data_loyalty():
    url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'
    try:
        df = pd.read_csv(url)
        # 1. Rename columns (ADJUST THIS LIST TO 11 NAMES)
        df.columns = [
            "Customer ID", "Age", "Gender", "Item Purchased", "Category", "Purchase Amount (USD)",
            "Location", "Size", "Color", "Season", "Review Rating" # List stops here (11 elements)
            # You must remove the remaining 7 column names
        ]
        
        # Data Transformation
        df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
        df['Subscription Status'] = df['Subscription Status'].map({1: 'Subscribed', 0: 'Non-Subscribed'})
        df['Discount Applied'] = df['Discount Applied'].map({1: 'Discount Applied', 0: 'No Discount'})
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_and_process_data_loyalty()

if df.empty:
    st.stop()

# --- Plotly Visualizations ---

frequency_order = ['Annually', 'Quarterly', 'Monthly', 'Fortnightly', 'Weekly', 'Daily']

st.header("1. Subscription Status vs Purchase Frequency (Count)")
# 1. Stacked Bar Chart for Subscription vs Purchase Frequency
fig1 = px.bar(
    df.sort_values('Frequency of Purchases', key=lambda x: x.map({v: i for i, v in enumerate(frequency_order)})),
    x='Subscription Status', color='Frequency of Purchases',
    title='Subscription Status vs Purchase Frequency',
    category_orders={"Frequency of Purchases": frequency_order},
    color_discrete_sequence=px.colors.qualitative.Plotly 
)
fig1.update_layout(yaxis_title="Count")
st.plotly_chart(fig1, use_container_width=True) # CORRECTED


st.header("2. Category vs Purchase Frequency (Count)")
# 2. Stacked Bar Chart (Category vs Purchase Frequency)
fig2 = px.bar(
    df.sort_values('Frequency of Purchases', key=lambda x: x.map({v: i for i, v in enumerate(frequency_order)})),
    x='Category', color='Frequency of Purchases',
    title='Category vs Purchase Frequency',
    category_orders={"Frequency of Purchases": frequency_order},
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig2.update_layout(yaxis_title="Count")
st.plotly_chart(fig2, use_container_width=True) # CORRECTED


st.header("3. Density Heatmap: Purchase Frequency vs Purchase Amount")
# 3. Heatmap for Purchase Frequency vs Purchase Amount
fig3 = px.density_heatmap(
    df, x='Purchase Amount (USD)', y='Frequency of Purchases',
    title='Density Heatmap: Purchase Frequency vs Purchase Amount',
    category_orders={"y": frequency_order},
    color_continuous_scale="Viridis" 
)
fig3.update_layout(yaxis={'categoryorder': 'array', 'categoryarray': frequency_order})
st.plotly_chart(fig3, use_container_width=True) # CORRECTED


st.header("4. Relationship: Previous Purchases vs Purchase Amount")
# 4. Scatter Plot with Line of Best Fit: Previous Purchases vs Purchase Amount
fig4 = px.scatter(
    df, x='Previous Purchases', y='Purchase Amount (USD)',
    title='Relationship: Previous Purchases vs Purchase Amount',
    opacity=0.6,
    trendline='ols', 
    trendline_color_override='green'
)
st.plotly_chart(fig4, use_container_width=True) # CORRECTED


st.header("5. Distribution of Subscription Status (Count)")
# 5. Histogram of Subscription
fig5 = px.histogram(
    df, x='Subscription Status',
    title='Distribution of Subscription Status',
    color='Subscription Status',
    color_discrete_map={'Subscribed': 'skyblue', 'Non-Subscribed': 'lightcoral'}
)
fig5.update_layout(yaxis_title="Count")
st.plotly_chart(fig5, use_container_width=True) # CORRECTED


st.header("6. Stacked Histogram: Purchase Frequency vs Previous Purchases (Count)")
# 6. Stacked Histogram of Purchase Frequency vs Previous Purchases
fig6 = px.histogram(
    df, x='Previous Purchases', color='Frequency of Purchases',
    title='Stacked Histogram: Previous Purchases vs Purchase Frequency',
    category_orders={"color": frequency_order},
    color_discrete_sequence=px.colors.qualitative.Bold,
    barmode='stack',
    nbins=10 
)
fig6.update_layout(yaxis_title="Count")
st.plotly_chart(fig6, use_container_width=True) # CORRECTED
