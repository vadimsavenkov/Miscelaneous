import pandas as pd
dataset = pd.read_csv('data/gpa.csv')

x_columns = 1
x = dataset.iloc[:, 0:x_columns].values
y = dataset.iloc[:, x_columns].values

