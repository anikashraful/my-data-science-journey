import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load telecom churn CSV (columns: CustomerID, Tenure, InternetService, PaymentMethod, Churn)
df = pd.read_csv('customer_churn.csv')

# Basic inspection
print(df.info())
print(df.isnull().sum())
print(df['Churn'].value_counts())

# Visualize churn distribution
sns.countplot(x='Churn', data=df, palette='coolwarm')
plt.title('Churn Distribution')
plt.show()

# Mean tenure of churned vs not churned
print(df.groupby('Churn')['Tenure'].mean())
