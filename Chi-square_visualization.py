# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:22:47 2020

@author: adars
"""


# import exploration files 
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
from sklearn.ensemble import RandomForestRegressor 
from scipy import stats
  


# In[2]:


file_path = '.csv'


# In[3]:


data = pd.read_csv(file_path)


# In[4]:


data.shape


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.describe(include = 'all')


# In[8]:


data.info()


# In[9]:


data.columns


# In[10]:


data.drop([""], axis = 1, inplace = True)


# In[11]:


data.head()


# In[12]:


dummy = pd.get_dummies(data[''])


# In[13]:


dummy.head()


# In[14]:


dummy_Marital_status = pd.get_dummies(data[''])


# In[15]:


dummy_Marital_status.head()


# In[16]:


data = pd.concat([data,dummy],axis=1)


# In[17]:


data.drop([''],axis=1,inplace = True)


# In[18]:


data.head()


# In[19]:


data = pd.concat([data,dummy_Marital_status],axis=1)


# In[20]:


data.drop([''],axis=1,inplace=True)


# In[21]:


data.head()


# In[22]:


data.columns


# In[23]:


data.hist() 


# In[24]:


#rows and columns returns (rows, columns)
data.shape


# In[25]:


data.columns


# In[26]:



sns.boxplot( x = "", y = "", data=data)


# In[27]:


plt.figure(figsize=(15,5))


# In[28]:


sns.boxplot( x = "Married", data=data)


# In[29]:


data.columns


# In[30]:


sns.boxplot(x = "NL_JK", y = "Married" , data=data)


# In[31]:


sns.boxplot(x = "NL_JK" , y = "Unmarried", data=data)


# In[32]:


sns.boxplot(x = "NL_JK", y = "F", data=data)


# In[33]:


sns.boxplot(x = "NL_JK", y = "M", data=data)


# In[34]:


data.columns


# In[35]:


sns.boxplot( x = "Reason_JK", y = "F", data=data)


# In[36]:


sns.boxplot(x = "Reason_JK", y = "M", data=data)


# In[37]:


sns.boxplot(x = "Reason_JK", y = "Married", data=data)


# In[38]:


sns.boxplot(x = "Reason_JK", y = "Unmarried", data=data)


# In[39]:


data.columns


# In[40]:


sns.boxplot(x = "JK_Types", y = "Healthy_food", data=data)


# In[41]:


sns.boxplot( x = "JK_Types", data=data)


# In[42]:


sns.boxplot( x =  'Unmarried', data=data)


# In[43]:


sns.lmplot(x="JK_Types",y="M",hue = "M", data=data,fit_reg=True,palette="Blues_d",lowess=True,scatter_kws={'alpha':0.5}, legend=True)


# In[44]:


sns.lmplot(x="JK_Types",y="F", hue = "F", data=data,fit_reg=True,palette="Blues_d")


# In[45]:


sns.lmplot(x="JK_Types",y="Married", hue = "Married",col = "Married", data=data,fit_reg=True,palette="Blues_d")


# In[46]:


sns.lmplot(x="JK_Types",y="Unmarried", hue = "Unmarried",col = "Unmarried", data=data,fit_reg=True,palette="Blues_d")


# In[47]:


sns.lmplot(x="What_you_pick",y="F", hue = "F",col = "F", data=data,fit_reg=True,palette="Blues_d")


# In[48]:


data.columns


# In[49]:


sns.lmplot(x="What_you_pick",y="M", hue = "M",col = "M", data=data,fit_reg=True,palette="Blues_d")


# In[50]:


sns.lmplot(x="What_you_pick",y="Married", hue = "Married",col = "Married", data=data,fit_reg=True,palette="Blues_d")


# In[51]:


sns.lmplot(x="What_you_pick",y="Unmarried", hue = "Unmarried",col = "Unmarried", data=data,fit_reg=True,palette="Blues_d")


# In[52]:


sns.boxplot( x = "What_you_pick", y = "M", data=data)


# In[53]:


sns.boxplot(x = "What_you_pick", y = "F", data=data)


# In[54]:


sns.boxplot( x = "M", y = "Married", data=data)


# In[55]:


sns.boxplot(x = "F" , y = "Unmarried", data=data)


# In[56]:


sns.boxplot( x = "M", y = "Unmarried", data=data)


# In[57]:


data.columns


# In[58]:


data['Healthy_food'].describe()   #RIGHT SKEWED


# In[59]:


data['Reason_JK'].describe()    #LEFT SKEWED


# In[60]:


data['JK_Types'].describe()   #RIGHT SKEWED


# In[61]:


data['Why_JK'].describe()   #RIGHT SKEWED


# In[62]:


data['Why_eat_JK'].describe()  #LEFT SKEWED


# In[63]:


data['Eat_JK_HF'].describe()   #LEFT SKEWED


# In[64]:


data['NL_JK'].describe()  #LEFT SKEWED


# In[65]:


data['JK_Quality'].describe()  #RIGHT SKEWED


# In[66]:


data['What_you_pick'].describe() #LEFT SKEWED


# In[67]:


data['F'].describe() #LEFT SKEWED


# In[68]:


data['M'].describe() #RIGHT SKEWED


# In[69]:


data['Married'].describe()  #RIGHT SKEWED


# In[70]:


data['Unmarried'].describe() #RIGHT SKEWED


# RANDOM FOREST

# In[71]:


x = data.iloc[:, 1:2].values  


# In[72]:


print(x)


# In[73]:


y = data.iloc[:, 2].values


# In[74]:


print(y)


# In[75]:


regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
  


# In[76]:


regressor.fit(x , y)


# In[77]:


Y_pred = regressor.predict(np.array([6.5]).reshape(1,1))


# In[78]:


X_grid = np.arange(min(x) , max(x), 0.01)


# In[79]:


X_grid = X_grid.reshape((len(X_grid), 1)) 


# In[80]:


plt.scatter(x,y,color = 'blue')


# In[81]:


plt.plot(X_grid, regressor.predict(X_grid),color = 'green')
plt.title('Random Forest Regression') 
plt.show()


# CHI-SQURE TEST - FEATURE SELECTION

# In[82]:


data_copy = data.copy()


# NULL HYPOTHESIS : THERE IS NO RELATIONSHIP BETWEEN TWO VALUES
# 
# ALTERNATE HYPOTHESIS : THERE IS A RELATIONSHIP BETWEEN TWO VALUES

# In[83]:


data['F'].value_counts()


# In[84]:


data['M'].value_counts()


# In[85]:


data['Unmarried'].value_counts()


# In[86]:


data['Married'].value_counts()


# In[87]:


data.columns


# 1. We have to find is there a relationship between Married preson Healthy_food ???
# 2. same as Unmarried person and Healthy_food how they relate or not ???
# 3. third question is about Female and NL_JK ???
# 4. and same see the relationship between Male and NL_JK ???

# In[88]:


married_Healthy_food = pd.crosstab(index=data['Married'],columns=data['Healthy_food'])


# In[89]:


married_Healthy_food


# In[90]:


married_Healthy_food.iloc[1].values


# In[91]:


married_Healthy_food.iloc[0].values


# In[92]:


(chi2, p , dof,_) = stats.chi2_contingency([married_Healthy_food.iloc[0].values,married_Healthy_food.iloc[1].values])


# In[93]:


print("chi2               : " , chi2)
print("p-value            : " , p)
print("Degrees of freedom : " , dof)


# In this case the p-value is 0.87 is greater than 0.05.Thus, we can say that there is no association between Married person and symbolize quality. That is reject Null hypothesis.

# In[94]:


Unmarried_Healthy_food = pd.crosstab(index=data['Unmarried'],columns=data['Healthy_food'])


# In[95]:


Unmarried_Healthy_food


# In[96]:


Unmarried_Healthy_food.iloc[0].values


# In[97]:


Unmarried_Healthy_food.iloc[1].values


# In[98]:


(chi2, p , dof,_) = stats.chi2_contingency([Unmarried_Healthy_food.iloc[0].values,Unmarried_Healthy_food.iloc[1].values])


# In[99]:


print("chi2               : " , chi2)
print("p-value            : " , p)
print("Degrees of freedom : " , dof)


# In this case the p-value is 0.87 is greater than 0.05.Thus, we can say that there is no association between Married person and symbolize quality. That is Accept Alternate hypothesis.

# In[100]:


Female_NL_JK =  pd.crosstab(index=data['F'],columns=data['NL_JK'])


# In[101]:


Female_NL_JK


# In[102]:


Female_NL_JK.iloc[0].values


# In[103]:


Female_NL_JK.iloc[1].values


# In[104]:


(chi2, p , dof,_) = stats.chi2_contingency([Female_NL_JK.iloc[0].values,Female_NL_JK.iloc[1].values])


# In[105]:


print("chi2               : " , chi2)
print("p-value            : " , p)
print("Degrees of freedom : " , dof)


# In this case the p-value is 0.60 is greater than 0.05.Thus, we can say that there is no association between Married person and symbolize quality. That is Accept Alternate hypothesis.

# In[106]:


Male_NL_JK =  pd.crosstab(index=data['M'],columns=data['NL_JK'])


# In[107]:


Male_NL_JK


# In[108]:


Male_NL_JK.iloc[0].values


# In[109]:


Male_NL_JK.iloc[1].values


# In[110]:


(chi2, p , dof,_) = stats.chi2_contingency([Male_NL_JK.iloc[0].values,Male_NL_JK.iloc[1].values])


# In[111]:


print("chi2               : " , chi2)
print("p-value            : " , p)
print("Degrees of freedom : " , dof)


# In this case the p-value is 0.60 is greater than 0.05.Thus, we can say that there is no association between Married person and symbolize quality. That is Accept Alternate hypothesis.

# In[113]:


data.columns


# In[115]:


data.drop(['Healthy_food'],axis=1,inplace=True)


# In[120]:


x = data['Eat_JK_HF']
y = data['F']
plt.bar(x,y)
plt.show()


# In[122]:


x = data['Eat_JK_HF']
y = data['M']
plt.bar(x,y)
plt.show()


# In[123]:


x = data['Eat_JK_HF']
y = data['Married']
plt.bar(x,y)
plt.show()


# In[124]:


x = data['Eat_JK_HF']
y = data['Unmarried']
plt.bar(x,y)
plt.show()


# In[125]:


x = data['Eat_JK_HF']
plt.hist(x)


# In[126]:


x = data['NL_JK']
plt.hist(x)


# In[127]:


x = data['Why_eat_JK']
plt.hist(x)
