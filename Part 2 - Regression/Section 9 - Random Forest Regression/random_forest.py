# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:31:37 2020

@author: Melody vilas pereira
"""
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#preprocessing
dataset=pd.read_csv('Position_Salaries.csv')

X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

#from sklearn.model_selection import test_train_split
#X_train,X_test,y_train,y_test=test_train_split(X,y,test_size=,random_state=0)


#Fitting the regression Model to dataset
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=300, random_state=0)
regressor.fit(X,y)
#create your regrssor here

# predicting a new result
y_pred=regressor.predict(6.5)


#Visualization steps
plt.scatter(X,y,color='red')
plt.plot(X,regressor.predict(X),color='blue')
plt.title('Truth or bluff{Random forest}')
plt.xlabel('Position')
plt.ylabel('Salaries')
plt.show()

#higher resolution results--much smoother curve
X_grid=np.arange(min(X),max(X),step=0.1)#this gives vector we need matrix
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Truth or bluff{Random forest regression}')
plt.xlabel('Position')
plt.ylabel('Salaries')
plt.show()



