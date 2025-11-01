import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

matplotlib.use('TkAgg')



customer_df = pd.read_csv('../../DataSet/Customers.csv')

# print("✅ Data Loaded:")
# print(customer_df.head())

clustering_features = [
    'Total Sales', 'Total Profit', 'Avg Discount', 'Total Quantity',
    'Num Orders', 'Customer Age (Days)', 'Recency (Days)'
]

clustering_data = customer_df[clustering_features].copy()

clustering_data = clustering_data.fillna(0)

# print("\n📊 Data ready for clustering:")
# print(clustering_data.describe())

scaler = StandardScaler()

scaled_data = scaler.fit_transform(clustering_data)

scaled_df = pd.DataFrame(scaled_data, columns=clustering_data.columns)

inertia = []

K_range = range(2, 11)

for k in K_range:

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)

    kmeans.fit(scaled_df)

    inertia.append(kmeans.inertia_)

# plt.figure(figsize=(8, 5))
#
# plt.plot(K_range, inertia, marker='o')
#
# plt.title('Elbow Method - Optimal Number of Clusters')
#
# plt.xlabel('Number of Clusters (K)')
#
# plt.ylabel('Inertia (Within Cluster Sum of Squares)')
#
# plt.grid(True)
#
# plt.show()

optimal_k = 4

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)

customer_df['Cluster'] = kmeans.fit_predict(scaled_df)

cluster_summary = customer_df.groupby('Cluster').agg({
    'Total Sales': 'mean',
    'Total Profit': 'mean',
    'Total Quantity': 'mean',
    'Customer Age (Days)': 'mean',
    'Recency (Days)': 'mean',
    'Churn': 'mean'
}).reset_index()

# print("✅ Cluster Summary:")
#
# print(cluster_summary)
#
# plt.figure(figsize=(8,6))
# sns.scatterplot(
#     x=customer_df['Total Sales'],
#     y=customer_df['Total Profit'],
#     hue=customer_df['Cluster'],
#     palette='viridis'
# )
# plt.title('Customer Segmentation based on Sales and Profit')
# plt.xlabel('Total Sales')
# plt.ylabel('Total Profit')
# plt.legend(title='Cluster')
# plt.tight_layout()
# plt.show()

cluster_insights = customer_df.groupby('Cluster').agg({
    'Total Sales': ['mean', 'sum', 'count'],
    'Total Profit': ['mean', 'sum'],
    'Recency (Days)': 'mean',
    'Customer Age (Days)': 'mean',
    'Churn': 'mean'
}).round(2)

# --- Add Cluster Labels ---
cluster_labels = {
    0: 'Core Loyal Customers',
    1: 'Lost or At-Risk Customers',
    2: 'High-Value Customers (VIPs)',
    3: 'Active Growing Customers'
}

customer_df['Cluster Label'] = customer_df['Cluster'].map(cluster_labels)

print(customer_df[['Customer ID', 'Cluster', 'Cluster Label']].head())

customer_df.to_csv('../../DataSet/Customer_Segmentation_Labeled.csv', index=False)
