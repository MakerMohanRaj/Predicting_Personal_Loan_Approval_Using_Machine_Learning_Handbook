# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nXwBefNR5Gb2GsHI64ApjcQtTdwoSime
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier,RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
import imblearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,f1_score

data = pd.read_csv('/content/loan_prediction.csv')
data

data['Gender']=data['Gender'].map({'Female':1,'Male':0})
data.head()

data['Property_Area']=data['Property_Area'].map({'Urban':2,'Semiurban':1,'Rural':0})
data.head()

data['Married']=data['Married'].map({'Yes':1,'No':0})
data.head()

data['Education']=data['Education'].map({'Graduate':1,'Not Graduate':0})
data.head()

data['Self_Employed']=data['Self_Employed'].map({'Yes':1,'No':0})
data.head()

data['Loan_Status']=data['Loan_Status'].map({'Y':1,'N':0})
data.head()

data.isnull().sum()



data['Gender']= data['Gender'].fillna(data['Gender']).mode()[0]

data['Married']= data['Married'].fillna(data['Married']).mode()[0]

data['Dependents']=data['Dependents'].str.replace('+','')

data['Dependents']=data['Dependents'].fillna(data['Dependents']).mode()[0]

data['Self_Employed']=data['Self_Employed'].fillna(data['Self_Employed']).mode()[0]

data['LoanAmount']=data['LoanAmount'].fillna(data['LoanAmount']).mode()[0]

data['Loan_Amount_Term']=data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term']).mode()[0]

data['Credit_History']=data['Credit_History'].fillna(data['Credit_History']).mode()[0]

data.isnull().sum()

data.info()

data['Gender']=data['Gender'].astype('int64')
data['Married']=data['Married'].astype('int64')
data['Dependents']=data['Dependents'].astype('int64')
data['Self_Employed']=data['Self_Employed'].astype('int64')
data['CoapplicantIncome']=data['CoapplicantIncome'].astype('int64')
data['Loan_Amount_Term']=data['Loan_Amount_Term'].astype('int64')
data['Credit_History']=data['Credit_History'].astype('int64')

data.info()

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(data['ApplicantIncome'],color='r')
plt.subplot(122)
sns.distplot(data['Credit_History'])

plt.figure(figsize=(18,4))
plt.subplot(1,4,1)
sns.countplot(data['Gender'])
plt.subplot(1,4,2)
sns.countplot(data['Education'])
plt.show()

plt.figure(figsize=(20,5))
plt.subplot(131)
sns.countplot(data['Married'], hue=data['Gender']())
plt.subplot(132)
sns.countplot(data['Self_Employed'], hue=data['Education']())
plt.subplot(133)
sns.countplot(data['Property_Area'], hue=data['Loan_Amount_Term'()])

pd.crosstab(data['Gender'],[data['Self_Employed']])

sns.swarmplot(data['Gender'],data['ApplicantIncome'], hue = data['Loan_Status'])

from imblearn.combine import SMOTETomek

smote = SMOTETomek()

y = data['Loan_Status']
x = data.drop(columns=['Loan_Status'],axis=1)

x.shape

y.shape

x_bal,y_bal = smote.fit_resample(x,y)

print(y.value_counts())
print(y_bal.value_counts())

names = x_bal.columns

x_bal.head()

sc=StandardScaler()
x_bal = sc.fit_transform(x_bal)

x_bal = pd.DataFrame(x_bal,columns=names)
x_bal.head()

x_train, x_test, y_train, y_test + train_test_split(x_bal,y_bal, test_size+0.33, random_state=42)

x_train.shape

x_test.shape

y_train.shape, y_test.shape



"""# **Model building**

"""

def RandomForest(x_train,x_train,y_test):
  model = RandomForestClassifier()
  model.fit(x_train,y_train)
  y_tr = model.predict(x_train)
  print(accuracy_score(y_tr,y_train))
  yPred = model.predict(X_test)
  print(accuracy_score(yPred,y_test))

RandomForest(x_train,x_test,y_train,y_test)

def decisionTree(x_train,x_test,y_train,y_test):
    model = DecisionTreeClassifier()
    model.fit(x_train,y_train)
    y_tr = model.predict(x_train)
    yPred = model.predict(x_tesst)
    print(accuracy_sscore(ypred,y_test))

decisionTree(x_train,x_test,y_train,y_test)

def KNN(x_train, x_test, y_train, y_test):
  knn + KNeighborsClassifier()
  knn.fit(x_train,y_train)
  yPred = knn.predict(x_test)
  print('***KNeighborsClassifier***')
  print('Confusion matrix')
  print(confusion_matrix(y_tesst,yPred))
  print('classification report')
  print(classification_report(y_test,yPred))

KNN(x_train,x_test,y_train,y_test)

def XGP(x_train,x_test,y_train,y_test):
    model = GradientBoostingClassifier()
    model.fit(x_train,y_train)
    y_tr = model.predict(x_train)
    print(accuracy_score(y_tr,y_train))
    yPred = model.predict(x_test)
    print(accuracy_score(yPred,y_test))

XGB(x_train,x_test,y_train,y_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras,layers import Dense

classifier = Sequential()
classifier.add(Dense(unitss=100,activation='relu',input_din-11))

classifier.add(Dense(units=50,activation='relu'))

classifier.add(Dense(units=1, activation='sigmoid'))

classifier.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

classifier.fix(x_train,y_train,batch_size=100,validation_split=0.2,epochs=100)

y_pred = classifier.predict(x_test)

y_pred

y_pred + y_pred.astype(int)
y_pred

print(accuracy_score(y_pred, y_test))
print("ANN Model")
print("Confusion_Matrix")
print(confusion_matrix(y_test, y_pred))
print("Classification Report")
print(classification_report(y_test, y_pred))



"""*hyper runnig pareametters*"""

rf = RandomForestClassifier()

from backcall.backcall import Parameter
Parameters ={
    'n_estimators' : [1,20,30,55,68,74,90,120,115],
    'criterion':['gini','entropy']
    'max_depth':[2,5,8,10],'verbose':[1,2,3,4,5,6,8,9,10]
}

RCV + RandomizedSearchCV(estimator=rf,param_distributions=Parameters,cv=10,n_iter=4)

RCV.fit(x_train,y_train)

bt_params =RCV.best_params_
bt_score = RCV.best_score_

bt_parms

bt_score

def RandomForest(x_train,x_test,y_train,y_test);
    model = RandomForestClassifier(verbose= ,n_estimators= , max_features='',max_depth=,criterion='')
    model.fit(x_train,y_train)
    y_tr = model.predict(x_train)
    print("Training Accuracy")
    print(accuracy_score(y_tr,y_train))
    yPred = model.predict(x_test)
    print('Testing Accuracy')
    print(accuracy_score(yPred,y_test))

model = RandomForestClassifier(verbose= , n_estimators= ,max_features= '',max_depth= ,criterion='')
model.fit(x_train,y_train)

RandomForest(x_train,x_test,y_train,y_test)



"""saving model"""

import pickle

pickel.dump(model,open('rdf','pkl','wb'))

