#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[7]:


concrete_data = pd.read_csv('Desktop/concrete_data.csv')


# In[8]:


concrete_data.head()


# # checking how many data points we have 

# In[9]:


concrete_data.shape


# In[10]:


concrete_data.describe()


# In[11]:


concrete_data.isnull().sum()


# # splitting data into predictors and targets

# In[12]:


concrete_data_columns = concrete_data.columns
predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # all columns except Strength
target = concrete_data['Strength'] # Strength column


# In[13]:


predictors.head()


# # normalizing the data by substracting the mean and dividing by the standard deviation.

# In[15]:


predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()


# In[16]:


n_cols = predictors_norm.shape[1] # number of predictors


# In[19]:


import keras


# # importing the rest of the packages from the Keras library that we will need to build our regressoin model.

# In[20]:


from keras.models import Sequential
from keras.layers import Dense


# # defining a function that defines our regression model for us so that we can conveniently call it to create our model.

# In[21]:


# define regression model
def regression_model():
    # create model
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))
    
    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


# # training and testing the network

# In[22]:


# build the model
model = regression_model()

# fit the model
model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)


# In[ ]:




