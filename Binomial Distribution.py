#!/usr/bin/env python
# coding: utf-8

# ######## BINOMIAL DISTRIBUTION ################

# Binomial distribution is a common discrete distribution used in statistics, as opposed to a continuous distribution, such as the normal distribution. This is because the binomial distribution only counts two states, typically represented as 1 (for a success) or 0 (for a failure) given a number of trials in the data

# ### DIFFERENCE BETWEEN BINOMIAL AND BERNOULLI DISTRIBUTION

# The Bernoulli distribution represents the success or failure of a single Bernoulli trial. The Binomial Distribution represents the number of successes and failures in n independent Bernoulli trials for some given value of n.

# A binomial experiment is an experiment where you have a fixed number of independent trials with only have two outcomes. For example, the outcome might involve a yes or no answer. If you toss a coin you might ask yourself “Will I get a heads?” and the answer is either yes or no.

# In[3]:


from numpy import random

x = random.binomial(n=10, p=0.5, size=20)

print(x)


# In[4]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()


# Difference Between Normal and Binomial Distribution
# The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.

# In[5]:


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()


# In[ ]:




