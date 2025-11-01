import streamlit as st
import pandas as pd

# Title of the app
st.title("🛍️ Consumer Shopping Behavior Analysis")

# Main Introduction Paragraph
st.write(
    """
    **Shopping Behavior Analysis** is a critical area for understanding consumer patterns and preferences. 🛒 By analyzing shopping behavior, businesses can optimize product offerings, personalize marketing strategies, and improve customer satisfaction. 💡
    This analysis explores various factors influencing shopping behavior, including **demographics**, **purchase frequency**, and **product categories**. With this information, businesses can tailor their approach to meet customer needs and enhance the shopping experience.
    """
)

# Project description
st.markdown("""
This app visualizes and analyzes customer shopping behavior based on demographic data, seasonal trends, and product preferences. 
Use it to uncover insights into purchasing patterns and consumer habits. 📊
""")

# Dataset Information
st.subheader("📦 Dataset Information")

st.markdown("""
The **Shopping Behaviour Dataset** is sourced from **Kaggle**, contributed by **Zubaira Maimona**, and was last updated two months ago. 📅 This dataset provides a comprehensive view of **consumer behavior** and **shopping patterns** across various **demographics**, **locations**, and **product categories** in the e-commerce sector. 🌍🛍️ It contains **3,900 customer records** and **18 attributes**, including key variables like **age**, **gender**, **location**, **purchase amount**, **payment method**, **product categories**, **seasonality**, and **promo code usage**. These attributes offer detailed insights into purchase details, shopping habits, and customer feedback, making it ideal for analyzing **consumer preferences** and **behaviours**.
""")

# Update objectives
st.write("### 🎯 Objectives of the Analysis")
st.write(
    """
    - **Objective 1**: To analyze the impact of demographic factors such as age, gender, and location on consumer shopping behavior, focusing on how these attributes influence purchase amounts and shopping frequency.
    - **Objective 2**: To investigate the effects of seasonality and discount applications on consumer purchasing behavior, examining how these factors alter purchase frequency and spending patterns across different periods.
    - **Objective 3**: To explore how product preferences and customer loyalty, including factors like previous purchases and subscription status, shape consumer purchasing decisions and overall buying behavior.
    """
)

# Dataset context and glossary
st.write("### 📝 Dataset Context")
st.write(
    """
    This dataset provides detailed insights into consumer behaviour and shopping patterns across various demographics, locations, and product categories. It contains 3,900 customer records with 18 attributes that describe purchase details, shopping habits, and preferences.
    
    The dataset includes information such as:
    
    - **Customer demographics** (Age, Gender, Location)
    - **Product details** (Item Purchased, Category, Size, Color, Season)
    - **Purchase information** (Purchase Amount (USD), Payment Method, Shipping Type)
    - **Shopping behaviour** (Frequency of Purchases, Previous Purchases, Subscription Status, Discount Applied, Promo Code Used)
    - **Customer feedback** (Review Rating)
    
    This dataset can be used to explore consumer decision-making and market trends, including:
    
    - How age, gender, or location influence shopping preferences.
    - The relationship between discounts, promo codes, and purchase amounts.
    - Which product categories and colors are most popular in different seasons.
    - Patterns in payment method usage (e.g., PayPal vs. Credit Card).
    - How subscription and loyalty behaviours affect shopping frequency.
    """
)

# Dataset Glossary: Column-wise
st.write("### 📝 Dataset Glossary (Column-wise)")

# Define the dataset columns, descriptions, and data types
column_info = {
    "Column Name": [
        "Customer ID", "Age", "Gender", "Item Purchased", "Category", "Purchase Amount (USD)",
        "Location", "Size", "Color", "Season", "Review Rating", "Subscription Status",
        "Shipping Type", "Discount Applied", "Promo Code Used", "Previous Purchases",
        "Payment Method", "Frequency of Purchases"
    ],
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
        "Indicates whether the customer has an active subscription with the store ('Yes'/'No').",
        "The type of delivery chosen, such as free shipping or express.",
        "Indicates whether a discount was applied during the purchase ('Yes'/'No').",
        "Shows whether the customer used a promotional code ('Yes'/'No').",
        "The number of items the customer has previously bought, reflecting loyalty.",
        "The payment method used (Credit Card, PayPal, etc.). Indicates financial behaviour.",
        "The frequency of purchases made by the customer, helping assess loyalty (e.g., 'Weekly', 'Quarterly')."
    ],
    "Data Type": [
        "Quantitative (Identifier)", 
        "Quantitative", 
        "Qualitative", 
        "Qualitative", 
        "Qualitative", 
        "Quantitative", 
        "Qualitative", 
        "Qualitative", 
        "Qualitative", 
        "Qualitative", 
        "Quantitative", 
        "Qualitative", 
        "Qualitative", 
        "Qualitative", 
        "Qualitative", 
        "Quantitative", 
        "Qualitative", 
        "Qualitative"
    ]
}

# Create a DataFrame
columns_df = pd.DataFrame(column_info)

# Display the table in Streamlit
st.write("### Dataset Column Descriptions")
st.dataframe(columns_df)
