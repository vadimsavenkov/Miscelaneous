# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:35:04 2019

@author: fjbel
"""

# part 1 build library, read data, encoding, split, train and test, feature scaler
# import libraries

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

dataset = pd.read_csv ('data_for_test.csv')
X = dataset.iloc[:, 3:13 ].values
Y = dataset.iloc[:, 13].values
#coding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:,1] = labelencoder_X_1.fit_transform(X[:,1])
labelencoder_X_2 = LabelEncoder()
X[:,2] = labelencoder_X_1.fit_transform(X[:,2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

#split the data into training and testing data
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

#feature scale for the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#part 2 build ann

import keras 
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

#add the first layer and first hidden layer

classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

#add the second layer

classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

#add the output layer

classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# compitle the ANN

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#fitting the network

classifier.fit(X_train, Y_train, batch_size = 100, epochs = 100)



#part 3 make the prediction and evaluate

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

#making the Confusion Matrix


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

print (cm)

