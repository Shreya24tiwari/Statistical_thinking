# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:46:48 2020

@author: adars
"""


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#%matplotlib inline
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
#from pandas_ml import ConfusionMatrix
from sklearn.metrics import classification_report as cr
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler 


file_path = '.csv'

# read in data 
data = pd.read_csv(file_path)


############################################################################## 
#Data Exploration
##############################################################################

#rows and columns returns (rows, columns)
data.shape

#returns the first x number of rows when head(num). Without a number it returns 5
data.head()

#returns the last x number of rows when tail(num). Without a number it returns 5
data.tail()

#returns an object with all of the column headers 
data.columns

#basic information on all columns 
data.info()

#gives basic statistics on numeric columns
data.describe()

#Drop that columns

data.columns
data.drop([""], axis = 1, inplace = True) 
data.head()



#Dummy variable

dummy = pd.get_dummies(data[''])
dummy.head()

dummy_Marital_status = pd.get_dummies(data[''])
dummy_Marital_status.head()


#Concatenate them on axis=1
data = pd.concat([data,dummy],axis=1)
data.drop([''],axis=1,inplace = True)
data.head()


data = pd.concat([data,dummy_Marital_status],axis=1)
data.drop([''],axis=1,inplace=True)
data.head()

#RENAME COLUMNS
#data = data.rename(columns={'18-24':'Age1','25-35':'Age2',36-50:'Age3'})
#print(data)

data.columns






#Gives basic statistics every columns
data.columns

data.describe(include = 'all')

#shows what type the data was read in as (float, int, string, bool, etc.)
data.dtypes

#shows which values are null
data.isnull()

#shows which columns have null values
data.isnull().any()

#shows for each column the percentage of null values 
data.isnull().sum() / data.shape[0]

#plot histograms for all numeric columns 
data.hist() 


#######################################################



############ RANDOM FOREST ###############



########################################################




x = data.iloc[:, 1:2].values  
print(x) 
y = data.iloc[:, 2].values 
print(y)

# Fitting Random Forest Regression to the dataset 
# import the regressor 
from sklearn.ensemble import RandomForestRegressor 
  
 # create regressor object 
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
  
# fit the regressor with x and y data 
regressor.fit(x, y)   

Y_pred = regressor.predict(np.array([6.5]).reshape(1, 1)) # test the output by changing values 


# Visualising the Random Forest Regression results 

# arange for creating a range of values 
# from min value of x to max 
# value of x with a difference of 0.01 
# between two consecutive values 
X_grid = np.arange(min(x), max(x), 0.01) 

# reshape for reshaping the data into a len(X_grid)*1 array, 
# i.e. to make a column out of the X_grid value				 
X_grid = X_grid.reshape((len(X_grid), 1)) 

# Scatter plot for original data 
plt.scatter(x, y, color = 'blue') 

# plot predicted data 
plt.plot(X_grid, regressor.predict(X_grid), 
		color = 'green') 
plt.title('Random Forest Regression') 
plt.show()
