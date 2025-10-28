import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../DataSet/Superstore.csv', encoding='latin1')

print(df.head())

print(df.shape)

print(df.describe())

print(df.info())

print(df.isnull().sum())


