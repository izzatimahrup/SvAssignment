import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Configuration and Data Loading ---
st.set_page_config(layout="wide")
st.title("👤 Demographic Analysis")
st.markdown("This section examines how demographic factors, such as age and gender, affect consumer shopping behavior, including purchase amounts and shopping frequency")

# 1. Cached Data Loading Function
@st.cache_data
def load_data(url):
    """Loads the shopping behavior data from a URL into a DataFrame."""
    try:
        df = pd.read_csv(url)
        # Convert Gender to string for better categorical plotting
        df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
        
        # --- MODIFICATION START ---
        # Convert Subscription Status to string (1: 'Yes', 0: 'No') as requested
        df['Subscription Status'] = df['Subscription Status'].map({1: 'Yes', 0: 'No'})
        # --- MODIFICATION END ---
        
        return df
    except Exception as e:
        st.error(f"An error occurred while reading the CSV from the URL: {e}")
        return pd.DataFrame()

# Define the URL
url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'

# Load the data into df
df = load_data(url)

# --- Plotly Visualizations ---

st.header("📊 Visualizations of Objectives 1")
st.markdown("To examine how key demographic factors like age, gender, and location influence consumer spending patterns and shopping frequency. By analyzing these variables, the study seeks to identify differences in purchasing behavior across various demographic groups.")

st.header("🔎 Summary")
st.markdown("The visualizations explore how age and gender influence consumer spending and shopping frequency. The box plot shows a higher purchase amount in older age groups, particularly those aged 36-45 and above. The bar chart comparing gender vs purchase amount reveals that males tend to spend slightly more than females on average. The purchase frequency vs gender stacked bar chart shows that both male and female shoppers exhibit similar frequencies of purchases, although there are slight variations in product category preferences. These findings indicate that age and gender both play a role in shaping consumer spending behavior, with older individuals and males spending more, but frequency remains consistent across gender.")

# Define the Age Group order for consistent plotting
age_order = ['18–25', '26–35', '36–45', '46–55', '56–65', '65+']

# 1. Box Plot for Age Group vs Purchase Amount (Interactive)
st.subheader("1. Purchase Amount Distribution by Age Group")
fig1 = px.box(
    df,
    x='Age Group',
    y='Purchase Amount (USD)',
    category_orders={"Age Group": age_order},
    title='Purchase Amount Distribution by Age Group',
    color='Age Group' # Add color for distinction
)
fig1.update_layout(xaxis={'categoryorder':'array', 'categoryarray':age_order}) # Enforce order
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# 2. Grouped Bar Chart of Age Group vs Category (Interactive)
st.subheader("2. Category Distribution by Age Group")

fig5 = px.histogram(
    df,
    x='Age Group',
    color='Category',
    category_orders={"Age Group": age_order},
    barmode='group',
    title='Category Distribution by Age Group '
)
fig5.update_layout(xaxis={'categoryorder':'array', 'categoryarray':age_order}) # Enforce order
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---") 

# 3. Stacked Bar Chart of Purchase Frequency vs Gender (Interactive)
st.subheader("3. Purchase Frequency vs. Gender")
gender_frequency_counts = df.groupby(['Frequency of Purchases', 'Gender'], observed=False).size().reset_index(name='Count')

fig3 = px.bar(
    gender_frequency_counts,
    y='Frequency of Purchases', # Y-axis for horizontal plot
    x='Count',
    color='Gender',
    orientation='h',
    title='Purchase Frequency vs. Gender ',
    color_discrete_map={'Female': 'lightpink', 'Male': 'steelblue'}
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

################################################################################################
# 2. Bar Chart of Gender vs Purchase Amount (Interactive)
st.subheader("2. Average Purchase Amount by Gender")
average_purchase_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean().reset_index()

fig2 = px.bar(
    average_purchase_by_gender,
    x='Gender',
    y='Purchase Amount (USD)',
    color='Gender',
    color_discrete_map={'Female': 'lightpink', 'Male': 'steelblue'}, # Use custom colors
    text=average_purchase_by_gender['Purchase Amount (USD)'].round(2), # Add labels
    title='Average Purchase Amount by Gender'
)
fig2.update_traces(textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# 3. Stacked Bar Chart of Purchase Frequency vs Gender (Interactive)
st.subheader("3. Purchase Frequency vs. Gender")
gender_frequency_counts = df.groupby(['Frequency of Purchases', 'Gender'], observed=False).size().reset_index(name='Count')

fig3 = px.bar(
    gender_frequency_counts,
    y='Frequency of Purchases', # Y-axis for horizontal plot
    x='Count',
    color='Gender',
    orientation='h',
    title='Purchase Frequency vs. Gender ',
    color_discrete_map={'Female': 'lightpink', 'Male': 'steelblue'}
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# 4. Stacked Bar Chart for Gender vs Subscription (Interactive)
st.subheader("4. Gender vs Subscription Status")
gender_subscription_counts = df.groupby(['Gender', 'Subscription Status'], observed=False).size().reset_index(name='Count')

fig4 = px.bar(
    gender_subscription_counts,
    x='Gender',
    y='Count',
    color='Subscription Status',
    title='Gender vs Subscription Status',
    labels={'Subscription Status': 'Subscription Status'},
    # Updated color map keys to match the new string values ('No' and 'Yes')
    color_discrete_map={'No': 'lightcoral', 'Yes': 'mediumseagreen'} 
)
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# 5. Grouped Bar Chart of Age Group vs Category (Interactive)
st.subheader("5. Category Distribution by Age Group")

fig5 = px.histogram(
    df,
    x='Age Group',
    color='Category',
    category_orders={"Age Group": age_order},
    barmode='group',
    title='Category Distribution by Age Group '
)
fig5.update_layout(xaxis={'categoryorder':'array', 'categoryarray':age_order}) # Enforce order
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# 6. Pie Chart of Gender (Interactive)
st.subheader("6. Distribution of Gender")
gender_counts = df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig6 = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Distribution of Gender ',
    color='Gender',
    color_discrete_map={'Female': 'lightpink', 'Male': 'steelblue'}
)
st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# 7. Histogram (Countplot) of Age Group (Interactive)
st.subheader("7. Distribution of Age Groups")

fig7 = px.histogram(
    df,
    x='Age Group',
    category_orders={"Age Group": age_order},
    color='Age Group',
    title='Distribution of Age Groups '
)
fig7.update_layout(xaxis={'categoryorder':'array', 'categoryarray':age_order}) # Enforce order
st.plotly_chart(fig7, use_container_width=True)
#################################################################################################
