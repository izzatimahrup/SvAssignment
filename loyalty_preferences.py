import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(layout="wide")
st.title("👑 Loyalty & Preferences Analysis")
st.markdown("This section examines how product preferences and customer loyalty influence consumer purchasing decisions, highlighting the role of previous purchases and subscription status.")

# --- Configuration and Data Loading ---

@st.cache_data
def load_and_process_data_loyalty():
    """Load and process the shopping behavior dataset"""
    url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'
    try:
        df = pd.read_csv(url)
        
        # Data Transformation - handle both numeric and string values
        if df['Gender'].dtype in ['int64', 'float64']:
            df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
        
        if df['Subscription Status'].dtype in ['int64', 'float64']:
            df['Subscription Status'] = df['Subscription Status'].map({1: 'Subscribed', 0: 'Non-Subscribed'})
        
        if df['Discount Applied'].dtype in ['int64', 'float64']:
            df['Discount Applied'] = df['Discount Applied'].map({1: 'Discount Applied', 0: 'No Discount'})
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# Load data
df = load_and_process_data_loyalty()

if df.empty:
    st.warning("No data available. Please check the data source.")
    st.stop()

# --- Define frequency order for consistent visualization ---
frequency_order = ['Annually', 'Quarterly', 'Monthly', 'Fortnightly', 'Weekly', 'Daily']

# --- Plotly Visualizations ---
st.header("📊 Visualizations of Objectives 3")
st.markdown("To explores how product preferences, such as item category and color, alongside customer loyalty factors like subscriptions and previous purchases, affect consumer decision-making. It aims to understand how loyalty and product choices influence overall purchase frequency and amounts spent.")

st.header("🔎 Summary")
st.markdown("This analysis explores customer loyalty and preference patterns. Subscribers show significantly higher purchase volume across all frequency categories, confirming that subscription status is a strong loyalty indicator. The data also reveals a positive correlation between purchase frequency and amount, meaning customers who shop more often tend to spend more per transaction. Conversely, the sheer number of previous purchases has a weaker direct correlation with the current purchase amount.")

# Define the Age Group order for consistent plotting

# 1. Subscription Status vs Purchase Frequency
st.header("1. Subscription Status vs Purchase Frequency (Count)")
try:
    fig1 = px.bar(
        df, 
        x='Subscription Status', 
        color='Frequency of Purchases',
        title='Subscription Status vs Purchase Frequency',
        category_orders={"Frequency of Purchases": frequency_order},
        color_discrete_sequence=px.colors.qualitative.Plotly,
        labels={'count': 'Count'}
    )
    fig1.update_layout(yaxis_title="Count", xaxis_title="Subscription Status")
    st.plotly_chart(fig1, use_container_width=True)
except Exception as e:
    st.error(f"Error creating chart 1: {e}")

# 2. Category vs Purchase Frequency
st.header("2. Category vs Purchase Frequency (Count)")
try:
    fig2 = px.bar(
        df, 
        x='Category', 
        color='Frequency of Purchases',
        title='Category vs Purchase Frequency',
        category_orders={"Frequency of Purchases": frequency_order},
        color_discrete_sequence=px.colors.qualitative.Pastel,
        labels={'count': 'Count'}
    )
    fig2.update_layout(yaxis_title="Count", xaxis_title="Category")
    st.plotly_chart(fig2, use_container_width=True)
except Exception as e:
    st.error(f"Error creating chart 2: {e}")

# 3. Density Heatmap: Purchase Frequency vs Purchase Amount
st.header("3. Density Heatmap: Purchase Frequency vs Purchase Amount")
try:
    fig3 = px.density_heatmap(
        df, 
        x='Purchase Amount (USD)', 
        y='Frequency of Purchases',
        title='Density Heatmap: Purchase Frequency vs Purchase Amount (Customer Count)', # Make title more descriptive
        color_continuous_scale="Plasma", # Change to 'Plasma' or 'Inferno' for better contrast in dark mode
        labels={'Purchase Amount (USD)': 'Purchase Amount (USD)', 'Frequency of Purchases': 'Purchase Frequency'},
        marginal_x='histogram', # Add marginal histograms for distribution context
        marginal_y='histogram'
    )
    # Ensure all text is readable in the dark theme
    fig3.update_layout(
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        yaxis={'categoryorder': 'array', 'categoryarray': frequency_order, 'title': 'Purchase Frequency'},
        xaxis={'title': 'Purchase Amount (USD)'}
    )
    # Add a note about the central finding (optional, based on data)
    fig3.add_annotation(
        text="Highest density indicates common customer behavior.", 
        xref="paper", yref="paper",
        x=0.5, y=-0.2, showarrow=False, font=dict(size=10, color="lightgray")
    )
    st.plotly_chart(fig3, use_container_width=True)
except Exception as e:
    st.error(f"Error creating chart 3: {e}")
    
# 4. Scatter Plot: Previous Purchases vs Purchase Amount
st.header("4. Relationship: Previous Purchases vs Purchase Amount")
try:
    fig4 = px.scatter(
        df, 
        x='Previous Purchases', 
        y='Purchase Amount (USD)',
        title='Relationship: Previous Purchases vs Purchase Amount (with OLS Trendline)', # Updated title
        opacity=0.4, # Decreased opacity slightly to better handle overplotting
        render_mode='webgl', # Recommended for large datasets in Plotly
        trendline='ols', 
        trendline_color_override='#FFD700', # Change to a brighter color like gold for dark mode visibility
        labels={'Previous Purchases': 'Previous Purchases', 'Purchase Amount (USD)': 'Purchase Amount (USD)'},
        # Add color to the points based on a third variable (e.g., 'Gender' or 'Subscription Status') for deeper insight
        # color='Subscription Status' 
    )
    
    fig4.update_traces(marker=dict(size=5, line=dict(width=0.5, color='DarkSlateGray'))) # Style the markers
    
    # Extract and display the R-squared value for the OLS trendline
    results = px.get_trendline_results(fig4)
    r_squared = results.iloc[0]["px_fit_results"].rsquared
    
    fig4.update_layout(
        xaxis_title="Previous Purchases", 
        yaxis_title="Purchase Amount (USD)",
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        # Annotate the R-squared value
        annotations=[
            dict(
                xref='paper', yref='paper',
                x=0.95, y=0.05,
                text=f'R-squared: {r_squared:.3f}', # Display R-squared near the bottom right
                showarrow=False,
                font=dict(color='white', size=12)
            )
        ]
    )
    st.plotly_chart(fig4, use_container_width=True)
except Exception as e:
    st.error(f"Error creating chart 4: {e}")
# 5. Distribution of Subscription Status
st.header("5. Distribution of Subscription Status (Count)")
try:
    fig5 = px.histogram(
        df, 
        x='Subscription Status',
        title='Distribution of Subscription Status',
        color='Subscription Status',
        color_discrete_map={'Subscribed': 'skyblue', 'Non-Subscribed': 'lightcoral'},
        labels={'count': 'Count'}
    )
    fig5.update_layout(yaxis_title="Count", xaxis_title="Subscription Status", showlegend=False)
    st.plotly_chart(fig5, use_container_width=True)
except Exception as e:
    st.error(f"Error creating chart 5: {e}")

# 6. Stacked Histogram: Purchase Frequency vs Previous Purchases
st.header("6. Stacked Histogram: Purchase Frequency vs Previous Purchases (Count)")
try:
    fig6 = px.histogram(
        df, 
        x='Previous Purchases', 
        color='Frequency of Purchases',
        title='Stacked Histogram: Previous Purchases vs Purchase Frequency',
        category_orders={"Frequency of Purchases": frequency_order},
        color_discrete_sequence=px.colors.qualitative.Bold,
        barmode='stack',
        nbins=10,
        labels={'count': 'Count'}
    )
    fig6.update_layout(yaxis_title="Count", xaxis_title="Previous Purchases")
    st.plotly_chart(fig6, use_container_width=True)
except Exception as e:
    st.error(f"Error creating chart 6: {e}")
