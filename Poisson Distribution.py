#!/usr/bin/env python
# coding: utf-8

# ######### POISSON DISTRIBUTION    ##########

# In statistics, a Poisson distribution is a statistical distribution that shows how many times an event is likely to occur within a specified period of time. It is used for independent events which occur at a constant rate within a given interval of time.

# Difference Between Normal and Poisson Distribution
# Normal distribution is continous whereas poisson is discrete.
# 
# But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.

# Poisson Distribution in simple way we can say that if I go out for a walk in twice today how is the Probability I will go tommorow for a walk Twice And Thrice or may be for once.....

# In[2]:


#Generate a random 1x30 distribution for occurence 3:

from numpy import random

x = random.poisson(lam=3, size=30)

print(x)


# In[3]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2, size=1000), kde=False)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




