#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as body


# In[ ]:


Diamond=body.read_csv('C:/Users/NITHISH/Desktop/Data Analytics/.idea/diamond.csv')


# In[ ]:


Diamond.mean()


# In[ ]:


Diamond.mean(axis=1)


# In[ ]:


Diamond.median()


# In[ ]:


max(Diamond['diamond price'])-min(Diamond['diamond price'])


# In[ ]:


body_quant=[Diamond['diamond price'].quantile(0),
            Diamond['diamond price'].quantile(0.25),
            Diamond['diamond price'].quantile(0.50),
            Diamond['diamond price'].quantile(0.75),
            Diamond['diamond price'].quantile(1)]


# In[ ]:


body_quant


# In[ ]:


Diamond['diamond price'].describe()


# In[ ]:


Diamond['diamond'].quantile(0.75)-Diamond['diamond price'].quantile(0.25)bodyfat['BodyFat'].kurt()


# In[ ]:


Diamnod['diamond price'].var()


# In[ ]:


Diamond['diamond price'].std()


# In[ ]:


abs_median=abs(Diamond['diamond price']-Diamond['diamond price'].median())


# In[ ]:


abs_median


# In[ ]:


med=abs_median.median()*1.4628


# In[ ]:


med


# In[ ]:


Diamond['diamond price'].skew()


# In[ ]:


bodyfat['BodyFat'].kurt()


# In[ ]:




