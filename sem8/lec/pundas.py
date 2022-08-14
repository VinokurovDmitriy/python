import pandas as pd
data = {
    'name': ['vassa', 'serwga', 'stepa'],
    'surname': ['ivanov', 'petrov', 'sidorov']
}
df = pd.DataFrame(data=data)
print(df)
df2 = pd.read_csv('test.csv')
print(df2)
