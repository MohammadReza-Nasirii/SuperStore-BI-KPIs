import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')

df = pd.read_csv('../DataSet/Superstore_Featured.csv')

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')

plt.title('Top 10 Selling Products')

plt.xlabel('Total Sales')

plt.ylabel('Product Name')

plt.tight_layout()

plt.show()

top_profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

sns.barplot(x=top_profit_products.values, y=top_profit_products.index, palette='crest')

plt.title('Top 10 Most Profitable Products')

plt.xlabel('Total Profit')

plt.ylabel('Product Name')

plt.tight_layout()

plt.show()

discount_per_product = df.groupby('Product Name')['Discount'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

sns.barplot(x=discount_per_product.values, y=discount_per_product.index, palette='magma')

plt.title('Top 10 Products by Average Discount')

plt.xlabel('Average Discount')

plt.ylabel('Product Name')

plt.tight_layout()

plt.show()

df['Profit Margin'] = df['Profit'] / df['Sales']

profit_margin = df.groupby('Product Name')['Profit Margin'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

sns.barplot(x=profit_margin.values, y=profit_margin.index, palette='coolwarm')

plt.title('Top 10 Products by Profit Margin')

plt.xlabel('Average Profit Margin')

plt.ylabel('Product Name')

plt.tight_layout()

plt.show()

sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(6,6))

plt.pie(sales_by_category.values, labels=sales_by_category.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))

plt.title('Sales Share by Category')

plt.tight_layout()

plt.show()
