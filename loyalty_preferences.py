import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- Configuration and Data Loading ---

url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'
df = pd.DataFrame() # Initialize empty DataFrame

try:
    # 1. Load the data
    df = pd.read_csv(url)

    # 2. Rename columns to match the Glossary/Visualizations
    df.columns = [
        "Customer ID", "Age", "Gender", "Item Purchased", "Category", "Purchase Amount (USD)",
        "Location", "Size", "Color", "Season", "Review Rating", "Subscription Status",
        "Shipping Type", "Discount Applied", "Promo Code Used", "Previous Purchases",
        "Payment Method", "Frequency of Purchases"
    ]

    # 3. Create the 'Age Group' column (though not explicitly used in this set, good practice)
    bins = [18, 26, 36, 46, 56, 66, 100]
    labels = ['18–25', '26–35', '36–45', '46–55', '56–65', '65+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # 4. Map numerical codes to string labels for plotting
    df['Gender'] = df['Gender'].map({1: 'Male', 0: 'Female'})
    df['Subscription Status'] = df['Subscription Status'].map({1: 'Subscribed', 0: 'Non-Subscribed'})
    df['Discount Applied'] = df['Discount Applied'].map({1: 'Discount Applied', 0: 'No Discount'})

    print("Data loaded and processed successfully.")

except Exception as e:
    print(f"An error occurred while reading the CSV from the URL: {e}")
    # Ensure df is an empty DataFrame if loading fails to prevent errors below
    df = pd.DataFrame()


# --- Interactive Plotly Visualizations (Objective 3 / Loyalty & Preferences) ---

if not df.empty:
    # Define a consistent order for Purchase Frequency
    frequency_order = ['Annually', 'Quarterly', 'Monthly', 'Fortnightly', 'Weekly', 'Daily']
    
    # 1. Stacked Bar Chart for Subscription vs Purchase Frequency
    fig1 = px.bar(
        df.sort_values('Frequency of Purchases', key=lambda x: x.map({v: i for i, v in enumerate(frequency_order)})),
        x='Subscription Status',
        color='Frequency of Purchases',
        title='1. Subscription Status vs Purchase Frequency (Interactive)',
        category_orders={"Frequency of Purchases": frequency_order},
        color_discrete_sequence=px.colors.qualitative.Plotly # Use a clear palette
    )
    # Customize layout for better readability
    fig1.update_layout(yaxis_title="Count")
    fig1.show()

    # ---
    # 2. Stacked Bar Chart (Category vs Purchase Frequency)
    fig2 = px.bar(
        df.sort_values('Frequency of Purchases', key=lambda x: x.map({v: i for i, v in enumerate(frequency_order)})),
        x='Category',
        color='Frequency of Purchases',
        title='2. Category vs Purchase Frequency (Interactive)',
        category_orders={"Frequency of Purchases": frequency_order},
        color_discrete_sequence=px.colors.qualitative.Pastel # Matching your original Pastel1 idea
    )
    fig2.update_layout(yaxis_title="Count")
    fig2.show()

    # ---
    # 3. Heatmap for Purchase Frequency vs Purchase Amount
    # Plotly does not have a direct `crosstab` heatmap like Seaborn, so we use a 2D histogram
    fig3 = px.density_heatmap(
        df,
        x='Purchase Amount (USD)',
        y='Frequency of Purchases',
        title='3. Density Heatmap: Purchase Frequency vs Purchase Amount (Interactive)',
        category_orders={"y": frequency_order},
        color_continuous_scale="Viridis" # A good continuous color scale
    )
    fig3.update_layout(yaxis={'categoryorder': 'array', 'categoryarray': frequency_order})
    fig3.show()

    # ---
    # 4. Violin Plot for Seasons vs Purchase Amount (Objective 2 overlap, but included here)
    fig4 = px.violin(
        df,
        x='Season',
        y='Purchase Amount (USD)',
        color='Season',
        box=True, # Add a box plot inside the violin
        points='outliers', # Show individual outliers
        title='4. Seasons vs Purchase Amount Distribution (Interactive)',
        color_discrete_sequence=px.colors.sequential.Agsunset # A cool, distinct seasonal palette
    )
    fig4.show()

    # ---
    # 5. Histogram of Subscription
    fig5 = px.histogram(
        df,
        x='Subscription Status',
        title='5. Distribution of Subscription Status (Interactive)',
        color='Subscription Status',
        color_discrete_map={'Subscribed': 'skyblue', 'Non-Subscribed': 'lightcoral'}
    )
    fig5.update_layout(yaxis_title="Count")
    fig5.show()

    # ---
    # 6. Scatter Plot with Line of Best Fit: Previous Purchases vs Purchase Amount
    # Replacing the simple line plot with a scatter plot and a trend line for relationship visualization
    fig6 = px.scatter(
        df,
        x='Previous Purchases',
        y='Purchase Amount (USD)',
        title='6. Relationship: Previous Purchases vs Purchase Amount (Interactive)',
        opacity=0.6,
        trendline='ols', # Add Ordinary Least Squares (linear) trendline
        trendline_color_override='green'
    )
    fig6.show()

    # ---
    # 7. Stacked Histogram of Purchase Frequency vs Previous Purchases
    fig7 = px.histogram(
        df,
        x='Previous Purchases',
        color='Frequency of Purchases',
        title='7. Stacked Histogram: Previous Purchases vs Purchase Frequency (Interactive)',
        category_orders={"color": frequency_order},
        color_discrete_sequence=px.colors.qualitative.Bold,
        barmode='stack',
        nbins=10 # Use 10 bins as in the original code
    )
    fig7.update_layout(yaxis_title="Count")
    fig7.show()
