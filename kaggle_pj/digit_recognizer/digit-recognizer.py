#!/usr/bin/env python
# coding: utf-8
base ='/Volumes/ModelY/Y-gitProject/macbook_intel_workspace/kaggle_pj/digit_recognizer'

import pandas as pd 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

train_read = pd.read_csv(base+"/input/train.csv")
train_read.head()

X_train = train_read.drop(columns=["label"])
Y_train = train_read["label"]
X_train.head()

# label是数字字符，作为目标结果，先分出来

Y_train


# In[6]:


testData = pd.read_csv(base+"/input/test.csv")
testData.head()


# In[7]:


X_test = testData


# In[8]:


X_test


# In[9]:


KNN = KNeighborsClassifier(n_neighbors=1)


# In[10]:


KNN.fit(X_train,Y_train)


# In[11]:


y_predict = KNN.predict(X_test)


# In[12]:


KNN.score(X_train,Y_train)


# In[13]:


y_predict


# In[14]:


ImageId = []
counter = 1
for i in y_predict:
    ImageId.append(counter)
    counter=counter+1


# In[15]:


finalSubmission = pd.DataFrame({"ImageId":ImageId, "Label":y_predict})


# In[16]:


finalSubmission


# In[17]:


finalSubmission.to_csv(base+'/output.csv',index=False)





