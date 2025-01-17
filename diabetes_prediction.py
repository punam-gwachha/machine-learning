# -*- coding: utf-8 -*-
"""diabetes prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VChNfLLxZBJkc9yIhEukJyZoOHk0dZ8r
"""



!pip install pandas



"""Importing the Dependencies"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score



"""Data collection and analysis

PIMA Diabetes Dataset
"""

#loading the diabetes dataset to a pandas Dataframe
diabetes_dataset=pd.read_csv('/content/diabetes.csv')

#printing the first five rows of the dataset
diabetes_dataset.head()

#number of rows and columns in this dataset
diabetes_dataset.shape

#getting the statistical message of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()



"""0--> non diabetic
1--> diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

# separating the data and labels
x= diabetes_dataset.drop(columns='Outcome',axis=1)
y=diabetes_dataset['Outcome']

print(x)

print(y)

#data preprocessing(standardization)
scaler=StandardScaler()

scaler.fit(x)

standardized_data=scaler.transform(x)

print(standardized_data)

x=standardized_data
y=diabetes_dataset['Outcome']

print(x)
print(y)



"""Train Test Split

"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

print(x.shape,x_train.shape,x_test.shape)



"""Training the model"""

classifier=svm.SVC(kernel='linear')

#training the support vector machine classifier
classifier.fit(x_train,y_train)



"""Model Evaluation

accuracy score
"""

#accuracy score on the training data
x_train_prediction=classifier.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)

print('accuracy score of the training data',training_data_accuracy)

#accuracy score on the test data
x_test_prediction=classifier.predict(x_test)
test_data_accuracy=accuracy_score(x_test_prediction,y_test)

print('accuracy score of the test data',test_data_accuracy)



"""Making a Predictive System"""

input_data=(4,110,92,0,0,37.6,0.191,30)

#changing the input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardize the input data
std_data=scaler.transform(input_data_reshaped)
print(std_data)

prediction= classifier.predict(std_data)
print(prediction)

if (prediction[0]==0):
  print('The person is not diabetic')
else:
    print('the person is diabetic')

input_data=(2,197,70,45,543,30.5,0.158,53)

#changing the input data to numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardize the input data
std_data=scaler.transform(input_data_reshaped)
print(std_data)

prediction= classifier.predict(std_data)
print(prediction)

if (prediction[0]==0):
  print('The person is not diabetic')
else:
    print('the person is diabetic')

