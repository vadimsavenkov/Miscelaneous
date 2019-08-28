import pandas as pd
dataset = pd.read_csv('data/gpa.csv')

x_columns  = 1
x = dataset.iloc[:,0:x_columns].values  # Read column 0 of dataset into X
y = dataset.iloc[:,x_columns].values    # Read column 1 of dataset into Y

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)

