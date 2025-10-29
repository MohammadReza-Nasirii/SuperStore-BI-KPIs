import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../DataSet/Superstore.csv', encoding='latin1')

# print(df.head())
#
# print(df.shape)
#
# print(df.describe())
#
# print(df.info())
#
# print(df.isnull().sum())

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year

df['Month'] = df['Order Date'].dt.month

df['Month_Name'] = df['Order Date'].dt.month_name()

df['Quarter'] = df['Order Date'].dt.quarter

df['Day_of_Week'] = df['Order Date'].dt.day_name()

df['Week_of_Year'] = df['Order Date'].dt.isocalendar().week

print(df[['Order Date', 'Year', 'Month', 'Month_Name', 'Quarter', 'Day_of_Week']].head(10))

