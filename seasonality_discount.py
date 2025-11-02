import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go # Retained for completeness

st.set_page_config(layout="wide")
st.title("🏷️ Season & Discount Analysis")
st.markdown("This section investigates how seasonality and the use of discounts impact consumer purchasing behavior, focusing on purchase frequency and spending patterns across different seasons.")

# --- Configuration and Data Loading ---

@st.cache_data
def load_and_process_data_seasonality():
    """Loads data from URL, processes columns, and prepares DataFrame."""
    url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'
    
    try:
        df = pd.read_csv(url)
        
        # Data Transformation
        df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
        df['Subscription Status'] = df['Subscription Status'].map({1: 'Subscribed', 0: 'Non-Subscribed'})
        df['Discount Applied'] = df['Discount Applied'].map({1: 'Discount Applied', 0: 'No Discount'})
        
        return df
    
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

df = load_and_process_data_seasonality()

if df.empty:
    st.stop()

# --- Plotly Visualizations ---

st.header("📊 Visualizations of Objectives 2")
st.markdown("To investigate how seasonal trends and the use of discount impact consumer purchasing behavior, particularly in terms of how often purchases are made and how much is spent. The analysis will look into how discounts and seasonal changes drive consumer decisions and spending habits.")

st.header("🔎 Summary")
st.markdown("The visualization explores the influence of Seasonality and Discount Application on purchase behavior. Discounts are applied to a significant portion of transactions (43%), establishing them as a key influence on purchase frequency. Analysis of spending patterns reveals that purchase amounts remain consistent across all four seasons, indicating that environmental changes have minimal influence on individual transaction value. Crucially, the average purchase amount is slightly lower when a discount is applied, suggesting that the current discount strategy is not effectively encouraging customers to increase their overall spending (basket size) per transaction.")

# --- Streamlit Page Content ---

discount_map = {'Discount Applied': '#1f77b4', 'No Discount': '#ff7f0e'}
season_order = ["Winter", "Spring", "Summer", "Fall"]


st.header("1. Discount Usage Distribution")
discount_counts = df['Discount Applied'].value_counts().reset_index()
discount_counts.columns = ['Discount Applied', 'Count']
fig1 = px.pie(discount_counts, names='Discount Applied', values='Count',
              title='Proportion of Purchases with Discount Applied', hole=0.4,
              color='Discount Applied', color_discrete_map=discount_map)
fig1.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig1, use_container_width=True) # CORRECTED

st.subheader("📝 Interpretation 1:")
st.markdown("""
The pie chart shows that 43% of customer transactions involve a discount, establishing a high baseline for discount usage frequency. This directly impacts the objective by confirming that discounts are a significant driver of individual purchase decisions, making them key to influencing customer behavior and transaction count.
""")
st.markdown("---")

st.header("2. Average Purchase Amount with/without Discount")
avg_purchase_discount = df.groupby('Discount Applied')['Purchase Amount (USD)'].mean().reset_index().round(2)
fig5 = px.bar(avg_purchase_discount, x='Discount Applied', y='Purchase Amount (USD)',
              color='Discount Applied', text='Purchase Amount (USD)',
              title='Average Purchase Amount by Discount Status', color_discrete_map=discount_map)
fig5.update_traces(textposition='outside')
fig5.update_layout(yaxis_title="Average Purchase Amount (USD)")
st.plotly_chart(fig5, use_container_width=True) # CORRECTED

st.subheader("📝 Interpretation 2:")
st.markdown("""
The bar chart reveals that the average customer spend per transaction is slightly lower when a discount is used $59.28 compared to a non-discounted transaction $60.15, a critical finding for analyzing spending patterns. The direct impact is that the current discount strategy is failing to motivate customers to add more items to their basket (up-sell) to increase their individual transaction value.
""")
st.markdown("---")

st.header("3. Purchase Amount Distribution by Season")
fig2 = px.violin(df, x='Season', y='Purchase Amount (USD)',
                 color='Season', box=True, points='outliers',
                 title='Purchase Amount Distribution by Season',
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 category_orders={"Season": season_order})
st.plotly_chart(fig2, use_container_width=True) # CORRECTED

st.subheader("📝 Interpretation 3:")
st.markdown("""
The violin plots show that the distribution of individual purchase amounts is stable across all four seasons (Q1-Q4). This directly supports the objective by indicating that seasonality does not influence how much a customer is willing to spend in a single transaction, suggesting that promotions should focus on what customers buy seasonally, rather than trying to change their total spending amount per visit.
""")
st.markdown("---")

# ####################################################################################################################
#st.header("1. Seasonal Discount Usage (Count)")
#season_discount_counts = df.groupby(['Season', 'Discount Applied'], observed=False).size().reset_index(name='Count')
#fig3 = px.bar(season_discount_counts, x='Season', y='Count',
#             color='Discount Applied', title='Discount Application Count by Season',
#             color_discrete_map=discount_map,
#             category_orders={"Season": season_order})
#st.plotly_chart(fig3, use_container_width=True) # CORRECTED
 
#st.header("2. Purchase Amount Distribution by Season")
#fig2 = px.violin(df, x='Season', y='Purchase Amount (USD)',
#                color='Season', box=True, points='outliers',
#                title='Purchase Amount Distribution by Season',
#                color_discrete_sequence=px.colors.sequential.Agsunset,
#                category_orders={"Season": season_order})
#st.plotly_chart(fig2, use_container_width=True) # CORRECTED


#st.header("3. Seasonal Discount Usage (Count)")
#season_discount_counts = df.groupby(['Season', 'Discount Applied'], observed=False).size().reset_index(name='Count')
#fig3 = px.bar(season_discount_counts, x='Season', y='Count',
#             color='Discount Applied', title='Discount Application Count by Season',
#              color_discrete_map=discount_map,
#             category_orders={"Season": season_order})
#st.plotly_chart(fig3, use_container_width=True) # CORRECTED


#st.header("4. Product Category Popularity by Season (Count)")
#fig4 = px.histogram(df, x='Season', color='Category',
#                    title='Product Category Counts by Season', barmode='group',
#                   category_orders={"Season": season_order})
#st.plotly_chart(fig4, use_container_width=True) # CORRECTED


#st.header("5. Average Purchase Amount with/without Discount")
#avg_purchase_discount = df.groupby('Discount Applied')['Purchase Amount (USD)'].mean().reset_index().round(2)
#fig5 = px.bar(avg_purchase_discount, x='Discount Applied', y='Purchase Amount (USD)',
#              color='Discount Applied', text='Purchase Amount (USD)',
#              title='Average Purchase Amount by Discount Status', color_discrete_map=discount_map)
#fig5.update_traces(textposition='outside')
#fig5.update_layout(yaxis_title="Average Purchase Amount (USD)")
#st.plotly_chart(fig5, use_container_width=True) # CORRECTED
# ####################################################################################################################
