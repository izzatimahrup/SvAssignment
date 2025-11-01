import streamlit as st

# Set up page configuration with Shopping Cart emoji as the icon
# FIX 1: Replace shortcode :shopping_cart: with literal emoji 🛒
st.set_page_config(
    page_title="Shopping Behaviour",  # Page title
    page_icon="🛒"  # Shopping Cart emoji as the icon
)

# Define pages with navigation
# The 'visualise' icon is already correct (📊)
visualise = st.Page('shopping_behaviour.py', title='Shopping Behaviour Visualization', icon='📊')

# FIX 2: Replace shortcode :house: with literal emoji 🏠
home = st.Page('home.py', title='HomePage', default=True, icon='🏠')

# Create a navigation structure
pg = st.navigation(
    {
        "Menu": [home, visualise]
    }
)

# Run the navigation
pg.run()
