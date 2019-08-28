"""
import pandas as pd
import numpy as np
"""

#import matplotlib.pyplot as plt
#import numpy as np
#import pandas as pd
"""2D plotting
setting colors to the plots, labeling and setting the labels different types of plot
x=[1,3,4,1.5] #x axis lb = 1 up = 4
y=[5,8,6,7] #y axis lower bound = 5 upper bound = 8
y2=[3,6,1,10] 

plt.plot(x,y, color='blue', label="Apple Prices")
plt.plot(x,y2, color='orange', label="Sumsung Prices")
plt.title("fig1) Comparison b/w orange and blue values")

plt.legend(loc="upper right") #upper/lower/left/right

plt.show() #it renders the screen

#help(plt.legend(loc=""))

counter=0
print(counter)
for i in range(10):
    counter+=1
print(counter)

x=[1,3,4,1.5] #x axis lb = 1 up = 4
y=[5,8,6,7] #y axis lower bound = 5 upper bound = 8
y2=[3,6,1,10] 

#locate plt.show in between to separate plots 
#plt.show() #it renders the screen

plt.scatter(x,y, color='blue', label="Apple Prices")
plt.scatter(x,y2, color='orange', label="Sumsung Prices")

plt.plot(x,y, color='blue', label="Apple Prices")
plt.plot(x,y2, color='orange', label="Sumsung Prices")

plt.title("fig1) Comparison b/w orange and blue values")  
        
plt.legend(loc="upper right") #upper/lower/left/right

aSeries=np.random.randint(1,5,5*5).reshape(5,5)
print(aSeries)

x=[1,3,4,1.5] #x axis lb = 1 up = 4
y=[5,8,6,7] #y axis lower bound = 5 upper bound = 8
y2=[3,6,1,10] 

plt.plot(x,y, color='blue', label="Apple Prices")
plt.plot(x,y2, color='orange', label="Sumsung Prices")
plt.title("fig1) Comparison b/w orange and blue values")

plt.legend(loc="upper right") #upper/lower/left/right


3D plotting


x=[1,3,4,1.5] #x axis lb = 1 up = 4
y=[5,8,6,7] #y axis lower bound = 5 upper bound = 8
y2=[3,6,1,10] 

plt.bar(x,y, color='blue', label="Apple Prices")
plt.bar(x,y2, color='orange', label="Sumsung Prices")

x=np.arange(20)
y=np.arange(40)
z=np.random.randint(1,40,20*40).reshape(40,20)

plt.countour(x,y,z)
plt.show()

#class Dog:
#    def __init__(self,_name):
#        self.name=_name
#    def values(self):
        
#testSubject1 = Dog("Boomer")
#testSubject2 = Dog("Benji")
#print(df)
#print(testSubject1.name)

"""
#df=pd.DataFrame({"Name":["Kanishqk", "Henry"], "ID":[20]})
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x=[1,2,5,2.5]
y=[3,8,1,6]
z=[[1,4,7,10],[3,5,11,7],[6,12,6,3],[3,2,8,9]]

#plt.contourf(x,y,z)

plt.contourf(np.arange(20), np.arange(40), np.random.randint(1,100,40*20).reshape(40,20))




#2D-plotting

#df=pd.DataFrame({"Year":[2000,2001,2002], "Prices":[200,190,205]})

#year=df.iloc[:,0].values  #first row to print
#prices=df.iloc[:,1].values  #first row to print
#print(prices)


#dt.month 1-12
#cat.codes() 0-11 range(0,12)
#mammal, bird, reptile

#plt.scatter(year, prices)

#class Dog:
#    def __init__(self,_name):
#        self.name=_name
#    def values(self):
        
#testSubject1 = Dog("Boomer")
#testSubject2 = Dog("Benji")
#print(df)
#print(testSubject1.name)



