import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')


df = pd.read_csv('../DataSet/Superstore_Featured.csv')

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

print(category_sales)

df['Profit Margin'] = df['Profit'] / df['Sales']

category_margin = df.groupby('Category')['Profit Margin'].mean().sort_values(ascending=False)

print(category_margin)

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print(top_products)

plt.figure(figsize=(7,5))

sns.scatterplot(x='Discount', y='Sales', data=df, alpha=0.6)

plt.title('Relationship Between Discount and Sales')

plt.xlabel('Discount')

plt.ylabel('Sales')

plt.show()

total_sales = df['Sales'].sum()

category_contrib = (category_sales / total_sales) * 100

print(category_contrib)

plt.figure(figsize=(8,5))

sns.barplot(x=category_sales.values, y=category_sales.index, palette='viridis')

plt.title('Total Sales by Category')

plt.xlabel('Total Sales')

plt.ylabel('Category')

plt.tight_layout()

plt.show()

plt.figure(figsize=(8,5))

sns.barplot(x=category_margin.values, y=category_margin.index, palette='magma')

plt.title('Average Profit Margin by Category')

plt.xlabel('Profit Margin')

plt.ylabel('Category')

plt.tight_layout()

plt.show()

