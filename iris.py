import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

def getCol(df,name):
    result=df[name]
    return result #result is the entries under the couomn name

def dimensions(df):
    return df.shape #attribute shape

def peek(df,n):
    return df.head(n)

def stats(df):
    return df.describe

def classCount(df):
    return df.count()

def histogram(df, var):
    p_df=df.groupby("class")
    #print(p_df)
    plt.hist(df[var])
    plt.title("RoboGarden Use Case")
    for group_name,group_data in p_df:
        print(group_name)
        print(group_data)
    plt.show() 
    
    for key,value in p_df:
     plt.title("Our Observation")
     plt.hist(value[var], label=key)
    plt.legend(loc="lower center")
    plt.show()    
    #print(p_df.sum()) 
    #plt.hist(df[var])

def main():
   headerNames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
   myData=pd.read_csv("iris.csv", names=headerNames)
   #print(getCol(myData, 'sepal-length'))
   #print(dimensions(myData))
   #print(peek(myData, 19))
   #print(stats(myData))
   #print((classCount(myData)))
   #plt.hist([1,3,4])
   #histogram(myData, 'sepal-length')
   x=[2,4,2,7] #1D list with len4
   y=[1,3.5,6,9]
   
   """
   (2,1)
   (4,3.5)
   (2,6)
   (7,9)
   """

   plt.scatter(x,y)
   plt.show()
   plt.scatter(np.random.randint(1,100,150), np.random.randint(1,100,150), color='green')
   plt.show()
   plt.scatter(np.random.randint(1,100,500), np.random.randint(1,100,500), color='red')

main()



