import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Function to load data
def load_data():
    data = pd.read_csv('main_data.csv')
    return data

# Function to create regression plot
def create_regression_plot(data):
    regplot_fig, ax = plt.subplots()
    sns.regplot(x='delivery_time', y='review_score', data=data, scatter_kws={'alpha': 0.3}, ax=ax)
    ax.set_xlabel('Delivery Time')
    ax.set_ylabel('Review Score')
    ax.set_title('Regression Plot: Delivery Time vs Review Score')
    ax.set_ylim(0, 6)
    st.pyplot(regplot_fig)

# Function to create box plot
def create_box_plot(data):
    boxplot_fig, ax = plt.subplots()
    sns.boxplot(x='review_score', y='delivery_time', data=data, ax=ax)
    ax.set_xlabel('Review Score')
    ax.set_ylabel('Delivery Time')
    ax.set_title('Box Plot: Review Score vs Delivery Time')
    st.pyplot(boxplot_fig)

# Function to create pie chart for order status percentage
def create_pie_chart(data):
    status_counts = data['order_status'].value_counts()
    plt.pie(status_counts, labels=None, startangle=90, counterclock=False)
    legend_labels = [f"{count} orders, {percentage:.1f}%" 
                     for count, percentage in zip(status_counts, status_counts / status_counts.sum() * 100)]
    plt.legend(legend_labels, bbox_to_anchor=(1, 0.5), loc="center left", fontsize=8)
    plt.title('Persentase Order Status')
    st.pyplot(plt)

# Function to create bar chart for top 10 order status
def create_bar_chart(data):
    status_counts = data['order_status'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(status_counts.index, status_counts.values, color=['green', 'blue', 'red', 'purple', 'orange', 'gray', 'brown', 'pink'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
    plt.xlabel('Status Order')
    plt.ylabel('Jumlah Pesanan')
    plt.title('Top 10 Status Order Berdasarkan Jumlah Pesanan')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

# Load data
all_df = load_data()

# Streamlit app
st.title('E-commerce Data Analysis')

# Sidebar
st.sidebar.title('Options')

# Sidebar navigation
page = st.sidebar.selectbox('Select a page', ['Welcome', 'Impact of Delivery Time', 'Order Status Percentage'])

# Main content
if page == 'Welcome':
    st.write("""
    This dashboard provides an opportunity to delve into e-commerce information.
    """)
    st.write("""
    Explore additional pages through the side navigation bar for more insightful data details.
    """)
elif page == 'Impact of Delivery Time':
    st.header('The Impact of Delivery Time to Review Score')
    
    # Dropdown to select plot type
    plot_type = st.selectbox('Select a plot type', ['Regression Plot', 'Box Plot'])

    # Plot selection
    if plot_type == 'Regression Plot':
        st.subheader('Regression Plot')
        create_regression_plot(all_df)
    elif plot_type == 'Box Plot':
        st.subheader('Box Plot')
        create_box_plot(all_df)

elif page == 'Order Status Percentage':
    st.header('The Percentage of Successful Deliveries to Customers')

    # Dropdown to select plot type
    plot_type_order_status = st.selectbox('Select a plot type', ['Pie Chart', 'Bar Chart'])

    # Plot selection for order status
    if plot_type_order_status == 'Pie Chart':
        st.subheader('Pie Chart: Order Status Percentage')
        create_pie_chart(all_df)
    elif plot_type_order_status == 'Bar Chart':
        st.subheader('Bar Chart: Top 10 Order Status')
        create_bar_chart(all_df)