import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuration and Data Loading ---
st.set_page_config(layout="wide")
st.title("🛒 Shopping Behavior Analysis")
st.markdown("A simple analysis of customer shopping data using Streamlit, Pandas, Matplotlib, and Seaborn.")

# 1. Cached Data Loading Function
# Use st.cache_data to prevent re-downloading the file on every interaction
@st.cache_data
def load_data(url):
    """Loads the shopping behavior data from a URL into a DataFrame."""
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"An error occurred while reading the CSV from the URL: {e}")
        return pd.DataFrame() # Return empty DataFrame on error

# Define the URL
url = 'https://raw.githubusercontent.com/izzatimahrup/SvAssignment/refs/heads/main/shopping_behaviour_cleaned.csv'

# Load the data
df = load_data(url)

# Exit if data loading failed
if df.empty:
    st.stop()

# Display the first few rows of the data
st.subheader("Raw Data Preview")
st.dataframe(df.head())

# --- Helper Function for Plotting ---

def add_value_labels(ax):
    """Adds labels to the end/center of the bars in a bar chart."""
    for container in ax.containers:
        # Use a consistent style for all bar labels
        try:
            ax.bar_label(container, fmt='%d', label_type='center', color='white')
        except ValueError: # Handle cases where bar_label might fail for certain plots (e.g., boxplot)
            pass

# Define custom colors
gender_colors = {1: 'blue', 0: 'pink'} # Assuming 1 is Male and 0 is Female
age_group_palette = sns.color_palette('bright')
category_palette = sns.color_palette('pastel')

# Define the Age Group order for consistent plotting
age_order = ['18–25', '26–35', '36–45', '46–55', '56–65', '65+']

# --- Visualizations ---

st.header("📊 Key Visualizations")
st.markdown("---")

# 1. Box Plot for Age Group vs Purchase Amount
st.subheader("1. Purchase Amount Distribution by Age Group")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Age Group', y='Purchase Amount (USD)', data=df, order=age_order, ax=ax1)
ax1.set_title('Purchase Amount Distribution by Age Group')
ax1.set_xlabel('Age Group')
ax1.set_ylabel('Purchase Amount (USD)')
st.pyplot(fig1)

st.markdown("---")

# 2. Bar Chart of Gender vs Purchase Amount
st.subheader("2. Average Purchase Amount by Gender")
average_purchase_by_gender = df.groupby('Gender')['Purchase Amount (USD)'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 6))
# Use list of colors based on order: [gender_colors[0], gender_colors[1]]
ax2 = sns.barplot(x='Gender', y='Purchase Amount (USD)', data=average_purchase_by_gender, palette=[gender_colors[0], gender_colors[1]], ax=ax2)
ax2.set_title('Average Purchase Amount by Gender')
ax2.set_xlabel('Gender')
ax2.set_ylabel('Average Purchase Amount (USD)')
ax2.set_xticklabels(['Female', 'Male'])
# Use bar_label for centered labels
for container in ax2.containers:
    ax2.bar_label(container, fmt='%.2f', label_type='center', color='white') # Use .2f for average value
st.pyplot(fig2)

st.markdown("---")

# 3. Stacked Bar Chart of Purchase Frequency vs Gender (with Frequency on y-axis)
st.subheader("3. Purchase Frequency vs. Gender")
gender_frequency_counts = df.groupby(['Frequency of Purchases', 'Gender'], observed=False).size().unstack(fill_value=0)
fig3, ax3 = plt.subplots(figsize=(10, 6))
custom_palette_3 = [gender_colors[0], gender_colors[1]]
ax3 = gender_frequency_counts.plot(kind='barh', stacked=True, color=custom_palette_3, ax=ax3)
ax3.set_title('Purchase Frequency vs. Gender')
ax3.set_xlabel('Count')
ax3.set_ylabel('Frequency of Purchases')
ax3.legend(title='Gender', labels=['Female', 'Male'])
for container in ax3.containers:
    ax3.bar_label(container, fmt='%d', label_type='center', color='white')
st.pyplot(fig3)

st.markdown("---")

# 4. Stacked Bar Chart for Gender vs Subscription
st.subheader("4. Gender vs Subscription Status")
gender_subscription_counts = df.groupby(['Gender', 'Subscription Status'], observed=False).size().unstack(fill_value=0)
fig4, ax4 = plt.subplots(figsize=(8, 6))
ax4 = gender_subscription_counts.plot(kind='bar', stacked=True, color=[gender_colors[0], gender_colors[1]], ax=ax4)
ax4.set_title('Gender vs Subscription Status')
ax4.set_xlabel('Gender')
ax4.set_ylabel('Count')
ax4.set_xticks(ticks=[0, 1], labels=['Female', 'Male'], rotation=0)
ax4.legend(title='Subscription Status', labels=['Non-Subscribed (0)', 'Subscribed (1)'])
for container in ax4.containers:
    ax4.bar_label(container, fmt='%d', label_type='center', color='white')
plt.tight_layout()
st.pyplot(fig4)

st.markdown("---")

# 5. Grouped Bar Chart of Age Group vs Category
st.subheader("5. Category Distribution by Age Group")
fig5, ax5 = plt.subplots(figsize=(10, 8))
ax5 = sns.countplot(data=df, x='Age Group', hue='Category', order=age_order, palette='tab10', ax=ax5)
ax5.set_title('Category Distribution by Age Group')
ax5.set_xlabel('Age Group')
ax5.set_ylabel('Count')
ax5.tick_params(axis='x', rotation=45)
ax5.legend(title='Category')
plt.tight_layout()
# Using a simpler label addition for this plot type
for container in ax5.containers:
    ax5.bar_label(container, fmt='%d', label_type='edge', padding=3, fontsize=8)
st.pyplot(fig5)

st.markdown("---")

# 6. Pie Chart of Gender
st.subheader("6. Distribution of Gender")
gender_counts = df['Gender'].value_counts().sort_index()
pie_labels = ['Female' if label == 0 else 'Male' for label in gender_counts.index]
pie_colors = [gender_colors[int(label)] for label in gender_counts.index]
fig6, ax6 = plt.subplots(figsize=(8, 8))
ax6.pie(gender_counts, labels=pie_labels, autopct='%1.1f%%', startangle=140, colors=pie_colors)
ax6.set_title('Distribution of Gender')
ax6.axis('equal')
st.pyplot(fig6)

st.markdown("---")

# 7. Histogram (Countplot) of Age Group
st.subheader("7. Distribution of Age Groups")
fig7, ax7 = plt.subplots(figsize=(10, 6))
ax7 = sns.countplot(x='Age Group', data=df, order=age_order, palette=age_group_palette, ax=ax7)
ax7.set_title('Distribution of Age Groups')
ax7.set_xlabel('Age Group')
ax7.set_ylabel('Count')
for container in ax7.containers:
    ax7.bar_label(container, fmt='%d')
st.pyplot(fig7)

# --- How to Run ---
st.sidebar.markdown(
    """
    **To run this Streamlit app:**
    1. Save the code above as a Python file (e.g., `app.py`).
    2. Open your terminal in the directory where you saved the file.
    3. Run the command: `streamlit run app.py`
    """
)
