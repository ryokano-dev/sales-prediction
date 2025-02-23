import pandas as pd

# data load
df = pd.read_csv('data/retail_sales_dataset.csv')
print('data overview')
print(df.describe())

# preprocess
df.dropna(inplace=True)
df.to_csv('data/preprocessed_sales.csv', index=False)
print('Successfully saved')
