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

print(kpi_summary)
