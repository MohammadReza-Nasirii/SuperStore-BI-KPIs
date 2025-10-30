import pandas as pd

df = pd.read_csv('../DataSet/Superstore_Featured.csv')

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()


# print(f"Total Sales: ${total_sales:,.2f}")
# print(f"Total Profit: ${total_profit:,.2f}")

avg_discount = df['Discount'].mean()
aov = df['Sales'].sum() / df['Order ID'].nunique()

# print(f"Average Discount: ${avg_discount:,.2f}")
# print(f"Average Oreder value: ${aov:,.2f}")

profit_margin = (total_profit / total_sales) * 100

# print(f"Profit Margin: ${profit_margin:,.2f}")

kpi_summary = pd.DataFrame({
    'KPI': ['Total Sales', 'Total Profit', 'Average Discount', 'Average Order Value', 'Profit Margin'],
    'Value': [f"${total_sales:,.2f}", f"${total_profit:,.2f}", f"{avg_discount:.2%}", f"${aov:,.2f}", f"{profit_margin:.2f}%"]
})

# print(kpi_summary)

region_kpi = df.groupby('Region').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean',
    'Order ID': pd.Series.nunique
}).reset_index()

region_kpi['AOV'] = region_kpi['Sales'] / region_kpi['Order ID']
region_kpi['Profit Margin (%)'] = (region_kpi['Profit'] / region_kpi['Sales']) * 100
region_kpi.rename(columns={'Discount': 'Avg Discount'}, inplace=True)

# print(region_kpi)

category_kpi = df.groupby('Category').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean',
    'Order ID': pd.Series.nunique
}).reset_index()

category_kpi['AOV'] = category_kpi['Sales'] / category_kpi['Order ID']
category_kpi['Profit Margin (%)'] = (category_kpi['Profit'] / category_kpi['Sales']) * 100
category_kpi.rename(columns={'Discount': 'Avg Discount'}, inplace=True)

# print(category_kpi)

segment_kpi = df.groupby('Segment').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean',
    'Order ID': pd.Series.nunique
}).reset_index()

segment_kpi['AOV'] = segment_kpi['Sales'] / segment_kpi['Order ID']
segment_kpi['Profit Margin (%)'] = (segment_kpi['Profit'] / segment_kpi['Sales']) * 100
segment_kpi.rename(columns={'Discount': 'Avg Discount'}, inplace=True)

# print(segment_kpi)
