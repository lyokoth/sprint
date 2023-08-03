import pandas as pd 

data = pd.read_csv('csv/200M_Male.csv')
print(data.columns)



data2 = pd.read_csv('csv/100M_Male.csv')
print(data2.columns)

data3 = pd.read_csv('csv/400_Male.csv')
print(data3.columns)