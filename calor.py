import pandas as pd

calories = {'Day 1': 1770, 'Day 2': 2210, 'Day 3': 1700}

series = pd.Series(calories)

print(series)
print(series.loc['Day 1'])