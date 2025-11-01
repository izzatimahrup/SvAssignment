import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --- Streamlit Setup ---
st.set_page_config(layout="wide")
st.title("🛍️ E-Commerce Data Visualization Dashboard")

# --- Dummy Data Load (Replace with your actual data loading) ---
# NOTE: Replace this section with how you load your actual 'df' (e.g., st.file_uploader or pd.read_csv)
try:
    # Attempt to load a sample dataset if df is not defined for testing
    df = pd.read_csv('https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv') # Replace 'your_data.csv' with your actual file path or loading method
except:
    st.warning("⚠️ Data could not be loaded. Please ensure your 'df' DataFrame is loaded correctly (e.g., using st.file_uploader or pd.read_csv).")
    # Creating a small dummy DataFrame for demonstration if the file isn't found
    data = {
        'Age Group': ['26–35', '18–25', '26–35', '46–55', '36–45', '65+', '56–65', '26–35'],
        'Purchase Amount (USD)': [50, 20, 150, 75, 90, 40, 60, 110],
        'Gender': [1, 0, 1, 0, 1, 0, 1, 0], # 1: Male, 0: Female
        'Frequency of Purchases': ['Annually', 'Monthly', 'Quarterly', 'Weekly', 'Daily', 'Annually', 'Monthly', 'Quarterly'],
        'Subscription Status': [1, 0, 1, 0, 1, 0, 1, 0], # 1: Subscribed, 0: Non-Subscribed
        'Category': ['Clothing', 'Footwear', 'Accessories', 'Beauty', 'Electronics', 'Clothing', 'Footwear', 'Accessories']
    }
    df = pd.DataFrame(data)
    st.info("Using a small dummy DataFrame for demonstration.")

# --- Helper Functions ---

# Function to add value labels to bars (re-defined to ensure Streamlit can run it)
def add_value_labels(ax, spacing=5):
    """Add labels to the end of the bars in a bar chart with value labels in white for center labels."""
    # Ensure this function is defined before its first use
    for container in ax.containers:
        # Check if the plot is a barplot (like plot 2) and apply center labels
        if any(bar.get_height() > 0 and len(ax.containers) == 1 for bar in container):
             ax.bar_label(container, fmt='%d', label_type='center', color='white')
        # For grouped bar charts (like plot 5) with 'edge' labels
        else:
             ax.bar_label(container, fmt='%d', label_type='edge', padding=3)

# Define custom colors
gender_colors = {1: 'blue', 0: 'pink'} # Assuming 1 is Male and 0 is Female
age_group_palette = sns.color_palette('bright')
category_palette = sns.color_palette('pastel')
frequency_palette = sns.color_palette('husl', len(df['Frequency of Purchases'].unique()))

# --- Visualization Sections (Using st.columns for better layout) ---

col1, col2 = st.columns(2)

with col1:
    ## 1. Box Plot for Age Group vs Purchase Amount
    st.subheader("1. Purchase Amount Distribution by Age Group 📦")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='Age Group', y='Purchase Amount (USD)', data=df,
                order=['18–25', '26–35', '36–45', '46–55', '56–65', '65+'], ax=ax1)
    ax1.set_title('Purchase Amount Distribution by Age Group')
    ax1.set_xlabel('Age Group')
    ax1.set_ylabel('Purchase Amount (USD)')
    st.pyplot(fig1)

with col2:
    ## 2. Bar Chart of Gender vs Purchase Amount
    st.subheader("2. Average Purchase Amount by Gender 💰")
    average_purchase_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Gender', y='Purchase Amount (USD)', data=average_purchase_by_gender,
                palette=[gender_colors[0], gender_colors[1]], ax=ax2)
    ax2.set_title('Average Purchase Amount by Gender')
    ax2.set_xlabel('Gender')
    ax2.set_ylabel('Average Purchase Amount (USD)')
    ax2.set_xticks(ticks=[0, 1], labels=['Female', 'Male'])
    add_value_labels(ax2)
    st.pyplot(fig2)

st.divider()

col3, col4 = st.columns(2)

with col3:
    ## 3. Stacked Bar Chart of Purchase Frequency vs Gender
    st.subheader("3. Purchase Frequency vs. Gender 📊")
    gender_frequency_counts = df.groupby(['Frequency of Purchases', 'Gender'], observed=False).size().unstack(fill_value=0)

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    gender_frequency_counts.plot(kind='barh', stacked=True, color=[gender_colors[0], gender_colors[1]], ax=ax3)
    ax3.set_title('Purchase Frequency vs. Gender')
    ax3.set_xlabel('Count')
    ax3.set_ylabel('Frequency of Purchases')
    ax3.legend(title='Gender', labels=['Female', 'Male'])

    # Add value labels
    for container in ax3.containers:
        ax3.bar_label(container, fmt='%d', label_type='center')
    st.pyplot(fig3)

with col4:
    ## 4. Stacked Bar Chart for Gender vs Subscription
    st.subheader("4. Gender vs Subscription Status ✅")
    gender_subscription_counts = df.groupby(['Gender', 'Subscription Status'], observed=False).size().unstack(fill_value=0)

    fig4, ax4 = plt.subplots(figsize=(8, 6))
    gender_subscription_counts.plot(kind='bar', stacked=True, color=[gender_colors[0], gender_colors[1]], ax=ax4)
    ax4.set_title('Gender vs Subscription Status')
    ax4.set_xlabel('Gender')
    ax4.set_ylabel('Count')
    ax4.set_xticks(ticks=[0, 1], labels=['Female', 'Male'], rotation=0)
    ax4.legend(title='Subscription Status', labels=['Non-Subscribed (0)', 'Subscribed (1)'])

    # Add value labels
    for container in ax4.containers:
        ax4.bar_label(container, fmt='%d', label_type='center')

    plt.tight_layout()
    st.pyplot(fig4)

st.divider()

col5, col6 = st.columns(2)

with col5:
    ## 5. Grouped Bar Chart of Age Group vs Category
    st.subheader("5. Category Distribution by Age Group 🛍️")
    fig5, ax5 = plt.subplots(figsize=(10, 8))
    sns.countplot(data=df, x='Age Group', hue='Category',
                  order=['18–25', '26–35', '36–45', '46–55', '56–65', '65+'],
                  palette='tab10', ax=ax5)
    ax5.set_title('Category Distribution by Age Group')
    ax5.set_xlabel('Age Group')
    ax5.set_ylabel('Count')
    ax5.tick_params(axis='x', rotation=45)
    ax5.legend(title='Category')
    plt.tight_layout()
    # Using the updated add_value_labels which applies 'edge' labels for countplot
    for container in ax5.containers:
         ax5.bar_label(container, fmt='%d', label_type='edge', padding=3)
    st.pyplot(fig5)

with col6:
    ## 6. Pie Chart of Gender
    st.subheader("6. Distribution of Gender 🚺🚹")
    gender_counts = df['Gender'].value_counts().sort_index()
    pie_labels = ['Female' if label == 0 else 'Male' for label in gender_counts.index]
    pie_colors = [gender_colors[int(label)] for label in gender_counts.index]

    fig6, ax6 = plt.subplots(figsize=(8, 8))
    ax6.pie(gender_counts, labels=pie_labels, autopct='%1.1f%%', startangle=140, colors=pie_colors)
    ax6.set_title('Distribution of Gender')
    ax6.axis('equal')
    st.pyplot(fig6)

st.divider()

## 7. Histogram of Age Group
st.subheader("7. Distribution of Age Groups 🎂")
fig7, ax7 = plt.subplots(figsize=(10, 6))
sns.countplot(x='Age Group', data=df,
              order=['18–25', '26–35', '36–45', '46–55', '56–65', '65+'],
              palette=age_group_palette, ax=ax7)
ax7.set_title('Distribution of Age Groups')
ax7.set_xlabel('Age Group')
ax7.set_ylabel('Count')
for container in ax7.containers:
    ax7.bar_label(container, fmt='%d')
st.pyplot(fig7)
