import streamlit as st
import pandas as pd

# Add a banner image at the top
banner_image = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i.jpeg' 
st.image(banner_image, use_container_width=True)

# Add the main introduction paragraph
st.write(
    """
    *Shopping Behavior Analysis* is a critical area for understanding consumer patterns and preferences. By analyzing shopping behavior, businesses can optimize product offerings, personalize marketing strategies, and improve customer satisfaction. 
    In this analysis, we explore various factors influencing shopping behavior, such as demographics, purchase frequency, and product categories.
    """
)

banner_image = 'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/main/3u1i_2.jpeg' 
st.image(banner_image, use_container_width=True)

# Update objectives
st.write("### Objectives of the Analysis")
st.write(
    """
    - **Objective 1**: To analyze how various demographic factors influence customer shopping behavior.
    - **Objective 2**: To investigate how seasonality and discount application influence consumer purchase frequency and amount.
    - **Objective 3**: To explore the influence of product preferences and customer loyalty on purchase behavior.
    """
)

# Dataset context and glossary
st.write("### Dataset Context")
st.write(
    """
    This dataset provides detailed insights into consumer behaviour and shopping patterns across various demographics, locations, and product categories. It contains 3,900 customer records with 18 attributes that describe purchase details, shopping habits, and preferences.
    
    The dataset includes information such as:
    
    - **Customer demographics** (age, gender, location)
    - **Product details** (item purchased, category, size, color, season)
    - **Purchase information** (amount spent in USD, payment method, shipping type)
    - **Shopping behaviour** (frequency of purchases, previous purchases, subscription status, discount usage, promo codes)
    - **Customer feedback** (review ratings)
    
    This dataset can be used to explore consumer decision-making and market trends, including:
    
    - How age, gender, or location influence shopping preferences.
    - The relationship between discounts, promo codes, and purchase amounts.
    - Which product categories and colors are most popular in different seasons.
    - Patterns in payment method usage (e.g., PayPal vs. Credit Card).
    - How subscription and loyalty behaviours affect shopping frequency.
    
    Researchers, data analysts, and students can use this dataset to practice customer segmentation, predictive modelling, recommendation systems, and market basket analysis. It also serves as a valuable resource for learning techniques in exploratory data analysis (EDA), machine learning, and business analytics.
    """
)

# Dataset Glossary: Column-wise
st.write("### Dataset Glossary (Column-wise)")

# Define the dataset columns, descriptions, and data types
column_info = {
    "Column Name": ["customer_id", "age", "gender", "item_purchased", "category", "purchase_amount_usd", "location", 
                    "size", "color", "season", "review_rating", "subscription_status", "shipping_type", 
                    "discount_applied", "promo_code_used", "previous_purchases", "payment_method", "frequency_of_purchases"],
    "Description": [
        "A unique identifier assigned to each customer. Helps distinguish shoppers.",
        "The age of the customer in years, useful for analyzing generational shopping habits.",
        "Gender of the customer (Male, Female). Helps understand gender-based buying trends.",
        "The specific product purchased by the customer, showing consumer demand.",
        "The broad classification of the purchased item, such as clothing or footwear.",
        "Total money spent on the purchase in USD. Reflects spending power.",
        "The state or region where the customer resides, useful for geographical patterns.",
        "The size of the purchased item (e.g., S, M, L). Indicates apparel preferences.",
        "The chosen color of the item. Reveals color preferences and trends.",
        "The season (Winter, Spring, etc.) when the purchase was made.",
        "A numerical rating reflecting the customer’s satisfaction with the product.",
        "Indicates whether the customer has an active subscription with the store.",
        "The type of delivery chosen, such as free shipping or express.",
        "Indicates whether a discount was applied during the purchase.",
        "Shows whether the customer used a promotional code.",
        "The number of items the customer has previously bought, reflecting loyalty.",
        "The payment method used (Credit Card, PayPal, etc.). Indicates financial behaviour.",
        "The frequency of purchases made by the customer, helping assess loyalty."
    ],
    "Data Type": ["Integer", "Integer", "String", "String", "String", "Float", "String", "String", "String", "String", "Float", "String", 
                  "String", "Boolean", "Boolean", "Integer", "String", "Integer"]
}

# Create a DataFrame
columns_df = pd.DataFrame(column_info)

# Display the table in Streamlit
st.write("### Dataset Column Descriptions")
st.dataframe(columns_df)

# Optionally, load and display the dataset (example path, you should replace with your actual dataset)
# data = pd.read_csv("shopping_behavior_data.csv")
# st.write("### Sample Data", data.head())
