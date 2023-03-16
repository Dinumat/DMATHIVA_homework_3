#!/usr/bin/env python
# coding: utf-8

# In[3]:


def findChar(a, b):
    return a[b-1]


# In[1]:


def doMath(c,d,e):
    x = e.count(d)
    result = c**3 + c/0.65 + x
    return result


# In[6]:


import csv
def fileInfo(f):
    with open('f.csv','r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        rows = sum(1 for row in csvreader)
        csvfile.seek(0) 
        cols = len(next(csv.reader(csvfile)))  
    return [rows, cols]




# In[ ]:




