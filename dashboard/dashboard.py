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

# Function to create bar chart
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

# Main content, information about dataset
if page == 'Welcome':
    st.write("""
    This dashboard provides an opportunity to delve into e-commerce information.
    """)
    st.write("""
    Explore additional pages through the side navigation bar for more insightful data details.
    """)
    st.header('About Dataset')
    st.write("""
    This dataset is a Brazilian ecommerce public dataset of orders made at Olist Store. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and reviews written by customers. There is also a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

    This is real commercial data, it has been anonymised, and references to the companies and partners in the review text have been replaced with the names of Game of Thrones great houses.
    """)
    st.subheader('Tables')
    st.write("""
    There are 9 tables:
    """)
    st.markdown('- customers')
    st.write('''
             contains: ('customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state')
             ''')
    st.markdown('- geolocation')
    st.write('''
             contains: ('geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state')
             ''')
    st.markdown('- orders')
    st.write('''
             contains: ('order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_customer_date', 'order_estimated_delivery_date')
             ''')
    st.markdown('- order_items')
    st.write('''
             contains: ('order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value')
             ''')
    st.markdown('- order_payments')
    st.write('''
             contains: ('order_id', 'payment_sequential', 'payment_type', 'payment_installments', 'payment_value')
             ''')
    st.markdown('- order_reviews')
    st.write('''
             contains: ('review_id', 'order_id', 'review_score', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp')
             ''')
    st.markdown('- products')
    st.write('''
             contains: ('product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm')
             ''')
    st.markdown('- product_category_name')
    st.write('''
             contains: ('product_category_name', 'product_category_name_english')
             ''')
    st.markdown('- sellers')
    st.write('''
             contains: ('seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state')
             ''')

#page information about impact of delivery time with data visualization
elif page == 'Impact of Delivery Time':
    st.header('The Impact of Delivery Time to Review Score')
    
    # Dropdown to select plot type
    plot_type = st.selectbox('Select a plot type', ['Regression Plot', 'Box Plot'])

    # Plot selection
    if plot_type == 'Regression Plot':
        st.subheader('Regression Plot')
        create_regression_plot(all_df)
        st.markdown('''
                    - The regression plot illustrates a discernible pattern between delivery time and review score.
                    ''')
        st.markdown('''
                    - The regression line suggests a negative correlation, indicating that higher review scores tend to be associated with shorter delivery times.
                    ''')
        st.markdown('''
                    - Specifically, the trend indicates that as delivery time decreases, the likelihood of receiving a higher review score increases.
                    ''')
        st.write('Conclusion :')
        st.markdown('''
                    - Instances with lower delivery times are more likely to result in favorable review scores, while higher delivery times may correlate with lower review scores.
                    ''')
        st.markdown('''
                    - Businesses might consider optimizing delivery processes to improve overall customer satisfaction, as indicated by the observed correlation between shorter delivery times and higher review scores.
                    ''')
        
    elif plot_type == 'Box Plot':
        st.subheader('Box Plot')
        create_box_plot(all_df)
        st.markdown('''
                    - The box plot provides insights into the distribution of delivery times across different review scores.
                    ''')
        st.markdown('''
                    - For a review score of 5, the box plot indicates a narrow distribution of delivery times with a low median. This suggests a consistent and shorter delivery time for customers providing the highest review score.
                    ''')
        st.markdown('''
                    - The narrow range and low median for review score 5 imply a higher level of consistency and efficiency in delivery times, contributing to the positive reviews.
                    ''')
        st.markdown('''
                    - Conversely, for lower review scores such as 1, the box plot shows a more varied distribution with a wider range and a higher median. This implies a greater variability in delivery times, potentially leading to longer delivery periods for customers who gave low scores.
                    ''')
        st.write('Conclusion :')
        st.markdown('''
                    - The higher review scores (e.g., 5) are associated with a more consistent and shorter delivery time. In contrast, lower review scores (e.g., 1) exhibit a wider range and longer delivery times, suggesting a connection between delivery efficiency and perceived customer satisfaction.
                    ''')
        st.markdown('''
                    - The observed patterns suggest a strong connection between customer satisfaction, as indicated by review scores, and the consistency and efficiency of delivery times. This insight can guide businesses in understanding the impact of delivery time on customer perceptions and optimizing their services accordingly.
                    ''')

#page information about order status percentage with data visualization
elif page == 'Order Status Percentage':
    st.header('The Percentage of Successful Deliveries to Customers')

    # Dropdown to select plot type
    plot_type_order_status = st.selectbox('Select a plot type', ['Pie Chart', 'Bar Chart'])

    # Plot selection for order status
    if plot_type_order_status == 'Pie Chart':
        st.subheader('Pie Chart: Order Status Percentage')
        create_pie_chart(all_df)
        st.markdown('''
                    - The pie chart reveals a significant success rate in delivering orders, with a percentage of 97%.
                    ''')
        st.markdown('''
                    - This high success rate signifies an efficient and successful product delivery process.
                    ''')
        st.markdown('''
                    - The notable success rate suggests a well-organized and effective system, contributing to positive customer experiences.
                    ''')
        st.write('Conclusion :')
        st.markdown('''
                    - The data implies that the majority of orders are successfully delivered, indicating optimal management of the delivery process.
                    ''')
    elif plot_type_order_status == 'Bar Chart':
        st.subheader('Bar Chart: Top 10 Order Status')
        create_bar_chart(all_df)
        st.markdown('''
                    - The bar chart provides a visual representation of the order status distribution, highlighting the top 10 order statuses.
                    ''')
        st.markdown('''
                    - "Delivered" emerges as the most prevalent status, indicating a high volume of successfully completed orders.
                    ''')
        st.markdown('''
                    - Following "Delivered," the status "Shipped" captures a substantial share of the order count, underlining the successful progression of shipped orders.
                    ''')
        st.markdown('''
                    - The presence of "Canceled" status in the top order statuses suggests a noteworthy number of cancellations, potentially indicating areas for improvement in order processing or customer communication.
                    ''')
        st.write('Conclusion :')
        st.markdown('''
                    - The distribution of order statuses, with "Delivered" standing out as the most prevalent status, followed by "Shipped" and "Canceled." This insight provides a quick overview of operational performance.
                    ''')
        st.markdown('''
                    - The high percentage of "Delivered" status may signify a high level of customer satisfaction, as orders are reaching customers successfully, contributing positively to the overall customer experience.
                    ''')