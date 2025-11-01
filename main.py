import streamlit as st

# Set up page configuration with Shopping Cart emoji as the icon
st.set_page_config(
    page_title="Shopping Behaviour",  # Page title
    page_icon="🛒"  # Shopping Cart emoji as the icon
)

# --- Define Pages with Navigation ---

# Home page (🏠: House/Home is universally recognized)
home = st.Page('home.py', title='HomePage', default=True, icon='🏠')

# Page for Objective 1: Demographic Analysis
# 👤: Bust/Silhouette is great for people/demographics.
visualise_demographics = st.Page('shopping_behaviour.py', title='Demographic Analysis', icon='👤')

# NEW PAGE 1 for Objective 2: Seasonality and Discounts
# 🏷️: Tag is perfect for 'Discounts'.
visualise_seasonality = st.Page('seasonality_discount.py', title='Season & Discount Analysis', icon='🏷️')

# NEW PAGE 2 for Objective 3: Loyalty and Preferences
# 👑: Crown/Gold Medal suggests 'Loyalty' or 'Premium status'.
visualise_loyalty = st.Page('loyalty_preferences.py', title='Loyalty & Preferences', icon='👑')

# --- Create a Navigation Structure ---

pg = st.navigation(
    {
        "Menu": [home, visualise_demographics, visualise_seasonality, visualise_loyalty]
    }
)

# Run the navigation
pg.run()
