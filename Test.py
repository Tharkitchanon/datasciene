import pandas as pd
data = pd.read_csv('l')
print(data)
print(data.info())
print(data.describe())
print("mean age = ",data['age'].mean())
print("mean gpa = ",data['gpa'].mean())
print("mean max = ",data['age'].mean())
print(data.loc[30:40])
print(data['age'].unique())
dataAge26=data[data['age']==26]
print(dataAge26)