import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [7,4,2,3,8,1]
y2 = [3,4,3,2,9,10]
#plt.plot(x,y)
plt.title("Custom Figure")
plt.xlabel("Horizontal Label")
plt.ylabel("Vertical Lable")
plt.plot(x,y,color= 'red',label= 'first y values')
plt.plot(x,y2,color= 'blue',label= 'second y values')
plt.legend(loc='upper left') #adding legend
plt.show()

