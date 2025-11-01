import streamlit as st

# Set up page configuration with Shopping Cart emoji as the icon
st.set_page_config(
    page_title="Shopping Behaviour",  # Page title
    page_icon=":shopping_cart:"  # Shopping Cart emoji as the icon
)

# Define pages with navigation
visualise = st.Page('shopping_behaviour.py', title='Shopping Behaviour Visualization', icon='📊')
home = st.Page('home.py', title='HomePage', default=True, icon=':house:')

# Create a navigation structure
pg = st.navigation(
    {
        "Menu": [home, visualise]
    }
)

# Run the navigation
pg.run()
