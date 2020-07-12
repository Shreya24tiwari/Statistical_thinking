#!/usr/bin/env python
# coding: utf-8

# ################### COVARIANCE ######################

# Covariance is a statistical tool that is used to determine the relationship between the movement of two asset prices. When two stocks tend to move together, they are seen as having a positive covariance; when they move inversely, the covariance is negative

# In[1]:


import numpy as np

A = [45,37,42,35,39]
B = [38,31,26,28,33]
C = [10,15,17,21,12]

data = np.array([A,B,C])

covMatrix = np.cov(data,bias=True)
print (covMatrix)


# In[2]:


import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

A = [45,37,42,35,39]
B = [38,31,26,28,33]
C = [10,15,17,21,12]

data = np.array([A,B,C])

covMatrix = np.cov(data,bias=True)
sn.heatmap(covMatrix, annot=True, fmt='g')
plt.show()


# To get the sample covariance (based on N-1), you’ll need to set the bias to False in the code below.
# 
# Here is the code based on the numpy package:

# In[3]:


import numpy as np

A = [45,37,42,35,39]
B = [38,31,26,28,33]
C = [10,15,17,21,12]

data = np.array([A,B,C])

covMatrix = np.cov(data,bias=False)
print (covMatrix)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




