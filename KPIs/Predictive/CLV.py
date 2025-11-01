import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')


df = pd.read_csv('../../DataSet/Superstore_Featured.csv')

customer_df = df.groupby('Customer ID').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean',
    'Quantity': 'sum',
    'Order ID': 'nunique',
    'Order Date': ['min', 'max']
}).reset_index()

customer_df.columns = ['Customer ID', 'Total Sales', 'Total Profit', 'Avg Discount', 'Total Quantity',
                       'Num Orders', 'First Purchase', 'Last Purchase']

customer_df['First Purchase'] = pd.to_datetime(customer_df['First Purchase'])
customer_df['Last Purchase'] = pd.to_datetime(customer_df['Last Purchase'])

customer_df['Customer Age (Days)'] = (customer_df['Last Purchase'] - customer_df['First Purchase']).dt.days

customer_df['Sales per Day'] = customer_df['Total Sales'] / (customer_df['Customer Age (Days)'] + 1)

# print(customer_df.head())

X = customer_df[['Num Orders', 'Avg Discount', 'Total Quantity', 'Customer Age (Days)', 'Sales per Day']]

y = customer_df['Total Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"MAE: {mae:.2f}")

print(f"RMSE: {rmse:.2f}")

importances = pd.DataFrame({

    'Feature': X.columns,

    'Importance': model.feature_importances_

}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(8,5))

sns.barplot(x='Importance', y='Feature', data=importances, palette='viridis')

plt.title('Feature Importance for CLV Prediction')

plt.tight_layout()

# plt.show()

