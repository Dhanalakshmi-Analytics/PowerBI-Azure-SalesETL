# Python script to clean sales data
import pandas as pd

df = pd.read_csv('../data/sample_sales.csv')
df.dropna(inplace=True)
df['Revenue_per_Unit'] = df['Revenue'] / df['Units']
df.to_csv('../data/cleaned_sales.csv', index=False)
