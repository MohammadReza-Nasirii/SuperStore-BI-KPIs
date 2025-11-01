import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

df = pd.read_csv('../../DataSet/Superstore_Featured.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'])

customer_df = df.groupby('Customer ID').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean',
    'Quantity': 'sum',
    'Order ID': 'nunique',
    'Order Date': ['min', 'max']
}).reset_index()

customer_df.columns = [
    'Customer ID', 'Total Sales', 'Total Profit', 'Avg Discount',
    'Total Quantity', 'Num Orders', 'First Purchase', 'Last Purchase'
]

customer_df['First Purchase'] = pd.to_datetime(customer_df['First Purchase'])
customer_df['Last Purchase'] = pd.to_datetime(customer_df['Last Purchase'])

current_date = df['Order Date'].max()

customer_df['Customer Age (Days)'] = (customer_df['Last Purchase'] - customer_df['First Purchase']).dt.days
customer_df['Recency (Days)'] = (current_date - customer_df['Last Purchase']).dt.days

customer_df['Churn'] = np.where(customer_df['Recency (Days)'] > 180, 1, 0)

print(customer_df[['Customer ID', 'Recency (Days)', 'Churn']].head(10))

X = customer_df[['Total Sales', 'Total Profit', 'Avg Discount', 'Total Quantity',
                 'Num Orders', 'Customer Age (Days)', 'Recency (Days)']]
y = customer_df['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBClassifier(
    objective='binary:logistic',
    eval_metric='logloss',
    random_state=42,
    learning_rate=0.05,
    n_estimators=200,
    max_depth=4
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
# print(f"✅ Accuracy: {acc:.2f}")

# print("\n📊 Classification Report:")
# print(classification_report(y_test, y_pred))
#
# cm = confusion_matrix(y_test, y_pred)
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
# plt.title('Confusion Matrix - Churn Prediction')
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.show()

customer_df.to_csv('../../DataSet/customers.csv', index=False)