#!/usr/bin/env python
# coding: utf-8

# In[1]:


greeting = 'hello, world'
chars = []
for l in greeting:
    chars.append(l)
chars


# In[2]:


chars = [l for l in greeting]
chars


# In[3]:


chars = [l for l in 'bla-bla-bla']
chars


# In[4]:


numbers = [n for n in range(0, 11)]
numbers


# In[5]:


numbers = [n*n for n in range(0, 11)]
numbers


# In[6]:


numbers = [n*n for n in range(0, 11) if n%2!=0]
numbers


# In[7]:


len_in_centimeters = [12,10,54,124,64]

len_in_inches = [(round(cm / 2.54, 2)) for cm in len_in_centimeters]
len_in_inches


# In[8]:


ratings = [2485, 2580, 2480, 2600, 2482, 2520]
titles = ['GM' if x >= 2500 else 'MM' for x in ratings]
titles


# In[9]:


#find all pairs sum of which equals 0
list1 = [2, 4, -5, 6, 8, -2,]
list2 = [2, -6, 8, 3, 5, -2,]

pairs = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
pairs


# In[11]:


pairs = [(x,y) for x in list1 for y in list2 if x+y==0]
pairs

