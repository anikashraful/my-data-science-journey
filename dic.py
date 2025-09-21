import pandas as pd

data = {
    'Name':['Spongebob','Patrick','Squidward'],
    'Age':[30, 36, 50]
}

df = pd.DataFrame(data, index=['Emp1','Emp2','Emp3'])

df['Job'] = ['Cook', 'Security', 'Cashier']

print(df)