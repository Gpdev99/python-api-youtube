import pandas as pd

obj = pd.read_json('data.json', orient='values')
print(obj)
obj.to_csv('dataCSV.csv')
