#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary libraries
import numpy as np
import cv2 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # loading out testing image

# In[2]:


#  Loading the image to be tested
test_image = cv2.imread('Desktop/pictures/jeff bezos.jpg')

# Converting to grayscale as opencv expects detector takes in input gray scale images
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Displaying grayscale image
plt.imshow(test_image_gray, cmap='gray')


# # color conversion

# In[3]:


def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# # loading Haar cascade classifier

# In[4]:


haar_cascade_face = cv2.CascadeClassifier('Desktop/CLONED FOLDER/Face-Detection-in-Python-using-OpenCV/data/haarcascades/haarcascade_frontalface_alt2.xml')


# In[5]:



faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

# Let us print the no. of faces found
print('Faces found: ', len(faces_rects))


# In[6]:


for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)


# In[7]:


#convert image to RGB and show image
plt.imshow(convertToRGB(test_image))


# In[8]:


def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 15)
        
    return image_copy


# In[9]:


#loading image
test_image2 = cv2.imread('Desktop/pictures/warren buffet.jpg')

#call the function to detect faces
faces = detect_faces(haar_cascade_face, test_image2)

#convert to RGB and display image
plt.imshow(convertToRGB(faces))


# # testing detection on a group picture

# In[10]:


#loading image
test_image2 = cv2.imread('Desktop/group picture 2.jpg')

#call the function to detect faces
faces = detect_faces(haar_cascade_face, test_image2)

#convert to RGB and display image
plt.imshow(convertToRGB(faces))


# In[ ]:




