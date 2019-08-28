#splitting the Date_Of_Birth date into date and time
#This is input 2018-03-04T19:00:00:000Z


temp_DOB=[]
date_temp=df.Date_Of_Birth.str.split("T")
for key, value in date_temp:
  temp_DOB.append(key)
print(temp_DOB)
df["Date_Of_Birth"]=temp_DOB

#This is output 2019-03-04