import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('../DataSet/Superstore_Featured.csv')

customer_kpis = df.groupby('Customer Name').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Order ID': 'nunique'
}).reset_index()

customer_kpis['AOV'] = customer_kpis['Sales'] / customer_kpis['Order ID']
customer_kpis['Profitability Ratio'] = customer_kpis['Profit'] / customer_kpis['Sales']

customer_kpis['CLV'] = customer_kpis['AOV'] * customer_kpis['Order ID']

top_customers_profit = customer_kpis.sort_values(by='Profit', ascending=False).head(10)
top_customers_sales = customer_kpis.sort_values(by='Sales', ascending=False).head(10)


repeat_customers = customer_kpis[customer_kpis['Order ID'] > 1].shape[0]
total_customers = customer_kpis.shape[0]
RPR = repeat_customers / total_customers
print(f"Repeat Purchase Rate (RPR): {RPR:.2%}")

customer_kpis['Avg_Profit_per_Order'] = customer_kpis['Profit'] / customer_kpis['Order ID']


scaler = MinMaxScaler()
customer_kpis[['Sales_norm', 'Profit_norm', 'Orders_norm']] = scaler.fit_transform(
    customer_kpis[['Sales', 'Profit', 'Order ID']]
)

customer_kpis['HVCI'] = (
    0.4 * customer_kpis['Sales_norm'] +
    0.4 * customer_kpis['Profit_norm'] +
    0.2 * customer_kpis['Orders_norm']
)

top_hv_customers = customer_kpis.sort_values(by='HVCI', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='CLV', y='Customer Name', data=customer_kpis.sort_values(by='CLV', ascending=False).head(10), palette='coolwarm')
plt.title('Top 10 Customers by Customer Lifetime Value')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='HVCI', y='Customer Name', data=top_hv_customers, palette='crest')
plt.title('Top 10 High Value Customers (HVCI)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='Sales', y='Customer Name', data=top_customers_sales, palette='magma')
plt.title('Top 10 Customers by Sales')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(x='Profit', y='Customer Name', data=top_customers_profit, palette='viridis')
plt.title('Top 10 Customers by Profit')
plt.tight_layout()
plt.show()

customer_kpis.to_csv('../DataSet/customer_kpis_full.csv', index=False)