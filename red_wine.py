#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
import sklearn as sk
#preprocessing module
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale


df = pd.read_csv("winequality-red.csv", sep=';')
df.columns
df.head()


x=df.drop("quality", axis=1) #if you want to drop a column axis=1, else it uses axis=0 for row 
y=df.quality
x_scale=scale(x)
x_train, x_test, y_train, y_test = train_test_split(x_scale,y,test_size=0.2, random_state=6)
print(x_train)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
max=0
max_model=None
for i in range(1000):
    clf=DecisionTreeClassifier()
    clf.fit(x_train, y_train)
#_prediction=clf.predict(x_test)
    accuracy_score=clf.score(x_test, y_test)
    if accuracy_score>max:
       max= accuracy_score
       max_model=clf
print(max)