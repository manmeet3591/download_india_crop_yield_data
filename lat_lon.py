#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium


# In[27]:


import pandas as pd
import numpy as np


# In[4]:


#pd.read_excel('tmp.xlsx', index_col=0)  # doctest: +SKIP


# In[20]:


File = "C:/Users/IITM/Downloads/crop_yield_district_india.xlsx"


# In[21]:


Data = pd.read_excel(File) 


# In[36]:


s = Data.iloc[:,0]
y = s[~s.isnull()]


# In[46]:


y.iloc[:].shape


# In[47]:


dis = y.values


# In[52]:


from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import csv
import sys


# In[ ]:




