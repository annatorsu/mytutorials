#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


img_raw=cv2.imread("Desktop/mandrill.jpg")


# In[6]:


type(img_raw)


# In[7]:


img_raw.shape


# In[8]:


plt.imshow(img_raw)


# In[21]:


img=cv2.cvtColor(img_raw,cv2.COLOR_BGR2RGB)
plt.imshow(img_raw)


# In[ ]:


import cv2

img=cv2.imread("Desktop/mandrill.jpg")

while True:
 
 cv2.imshow("mandrill",img)
    
 if cv2.waitKey(1) & 0XFF==27:
    
    break
    
    
    cv2.destroyAllWindows()


# In[ ]:




