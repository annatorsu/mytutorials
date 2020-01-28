#!/usr/bin/env python
# coding: utf-8

# In[2]:


import keras

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


# import the data
from keras.datasets import mnist

# read the data
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# In[5]:


X_train.shape


# In[6]:


plt.imshow(X_train[0])


# In[7]:


# flatten images into one-dimensional vector

num_pixels = X_train.shape[1] * X_train.shape[2] # find size of one-dimensional vector

X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32') # flatten training images
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32') # flatten test images


# In[8]:


# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255


# In[9]:


# one hot encode outputs
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

num_classes = y_test.shape[1]
print(num_classes)


# In[10]:


# define classification model
def classification_model():
    # create model
    model = Sequential()
    model.add(Dense(num_pixels, activation='relu', input_shape=(num_pixels,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    
    # compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


# In[11]:


# build the model
model = classification_model()

# fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)

# evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)


# # printing the accuracy and the corresponding error.

# In[12]:


print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))        


# # Sometimes, you cannot afford to retrain your model everytime you want to use it, especially if you are limited on computational resources and training your model can take a long time. Therefore, with the Keras library, you can save your model after training. To do that, we use the save method.

# In[13]:


model.save('classification_model.h5')


# # When you are ready to use your model again, you use the load_model function from <strong>keras.models</strong>.

# In[14]:


from keras.models import load_model


# In[15]:


pretrained_model = load_model('classification_model.h5')

