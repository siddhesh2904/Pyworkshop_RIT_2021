import pandas as pd

data=pd.read_csv("data/drinks.csv")

# print(data.head())


# print(data[data.country=='Yemen'])


print(data[data.country=='Yemen'].count())