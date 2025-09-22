import pandas as pd 

df = pd.read_csv('sales.csv')

print(df.describe())

revenue_by_product = df.groupby('Product')['Revenue'].sum()
print('Revenue by product:\n', revenue_by_product)

mean_quantity = df.groupby('Product')['Quantity'].mean()
print('Mean quantity sold by product:\n', mean_quantity)

import matplotlib.pyplot as plt
revenue_by_product.plot(kind='bar', title='Total:')
plt.ylabel('Revenue')
plt.show()