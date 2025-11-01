import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from IPython.display import display # Keep for display(df.head()) if running in Jupyter/Colab

# --- Configuration and Data Loading ---

url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'
df = pd.DataFrame() # Initialize empty DataFrame

try:
    # 1. Load the data
    df = pd.read_csv(url)



    # 3. Create the 'Age Group' column (Necessary for the visualizations)
    bins = [18, 26, 36, 46, 56, 66, 100]
    labels = ['18–25', '26–35', '36–45', '46–55', '56–65', '65+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # 4. Map numerical codes to string labels for plotting (necessary for Plotly)
    df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
    df['Subscription Status'] = df['Subscription Status'].map({1: 'Subscribed', 0: 'Non-Subscribed'})
    df['Discount Applied'] = df['Discount Applied'].map({1: 'Discount Applied', 0: 'No Discount'})

    print("Data loaded and processed successfully. Displaying first 5 rows:")
    # Use display(df.head()) if running in Jupyter/Colab
    # If running in a standard environment, use print(df.head().to_markdown(index=False))
    display(df.head())

except Exception as e:
    print(f"An error occurred while reading the CSV from the URL: {e}")


# --- Interactive Plotly Visualizations ---

if not df.empty:
    age_order = ['18–25', '26–35', '36–45', '46–55', '56–65', '65+']
    gender_colors = {'Male': '#1f77b4', 'Female': '#ff7f0e'}
    discount_map = {'Discount Applied': '#1f77b4', 'No Discount': '#ff7f0e'}


    # 1. Box Plot for Age Group vs Purchase Amount
    fig1 = px.box(
        df,
        x='Age Group',
        y='Purchase Amount (USD)',
        category_orders={"Age Group": age_order},
        title='1. Purchase Amount Distribution by Age Group (Interactive)',
        color='Age Group'
    )
    fig1.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': age_order})
    fig1.show()


    # 2. Bar Chart of Gender vs Purchase Amount (Aggregated)
    average_purchase_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean().reset_index().round(2)
    fig2 = px.bar(
        average_purchase_by_gender,
        x='Gender',
        y='Purchase Amount (USD)',
        color='Gender',
        color_discrete_map=gender_colors,
        text='Purchase Amount (USD)',
        title='2. Average Purchase Amount by Gender (Interactive)'
    )
    fig2.update_traces(textposition='outside')
    fig2.show()


    # 3. Stacked Bar Chart of Purchase Frequency vs Gender (Horizontal Stacked)
    gender_frequency_counts = df.groupby(['Frequency of Purchases', 'Gender'], observed=False).size().reset_index(name='Count')
    fig3 = px.bar(
        gender_frequency_counts,
        y='Frequency of Purchases',
        x='Count',
        color='Gender',
        orientation='h',
        title='3. Purchase Frequency vs Gender (Interactive)',
        color_discrete_map=gender_colors
    )
    fig3.show()


    # 4. Stacked Bar Chart for Gender vs Subscription
    gender_subscription_counts = df.groupby(['Gender', 'Subscription Status'], observed=False).size().reset_index(name='Count')
    fig4 = px.bar(
        gender_subscription_counts,
        x='Gender',
        y='Count',
        color='Subscription Status',
        title='4. Gender vs Subscription Status (Interactive)',
        color_discrete_map={'Subscribed': '#1f77b4', 'Non-Subscribed': '#ff7f0e'}
    )
    fig4.show()


    # 5. Grouped Bar Chart of Age Group vs Category
    fig5 = px.histogram(
        df,
        x='Age Group',
        color='Category',
        category_orders={"Age Group": age_order},
        barmode='group',
        title='5. Category Distribution by Age Group (Interactive)'
    )
    fig5.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': age_order})
    fig5.show()


    # 6. Donut Chart of Discount Applications
    discount_counts = df['Discount Applied'].value_counts().reset_index()
    discount_counts.columns = ['Discount Applied', 'Count']
    fig6 = px.pie(
        discount_counts,
        names='Discount Applied',
        values='Count',
        title='6. Discount Application Distribution (Interactive)',
        hole=0.3, # Creates the donut shape
        color='Discount Applied',
        color_discrete_map=discount_map
    )
    fig6.show()


    # 7. Line Chart for Purchase Amount (using histogram to get binned data)
    fig7 = px.histogram(
        df,
        x='Purchase Amount (USD)',
        nbins=10,
        title='7. Distribution of Purchase Amount (Binned) (Interactive)',
        color_discrete_sequence=['#1f77b4']
    )
    # Update traces to show as a smooth line/area instead of bars
    fig7.update_traces(kind='area', line={'shape': 'spline', 'width': 2})
    fig7.update_xaxes(title_text='Purchase Amount (USD) Bins')
    fig7.update_yaxes(title_text='Count')
    fig7.show()


    # 8. Bar Chart for Purchase Frequency
    purchase_frequency_counts = df['Frequency of Purchases'].value_counts().reset_index()
    purchase_frequency_counts.columns = ['Frequency of Purchases', 'Count']
    fig8 = px.bar(
        purchase_frequency_counts,
        x='Frequency of Purchases',
        y='Count',
        color='Frequency of Purchases',
        text='Count',
        title='8. Purchase Frequency Distribution (Interactive)'
    )
    fig8.update_traces(textposition='outside')
    fig8.show()
