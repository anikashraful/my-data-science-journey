import pandas as pd

data = [100.1, 102.2, 104.3]

series = pd.Series(data, index=['a', 'b', 'c'])

print(series)