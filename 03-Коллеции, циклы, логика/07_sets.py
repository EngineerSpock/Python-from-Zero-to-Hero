#!/usr/bin/env python
# coding: utf-8

# In[1]:


myset = set()
print(myset)
print(type(myset))


# In[2]:


myset.add(1)
myset


# In[3]:


myset.add(2)
myset


# In[4]:


myset.add(2)
myset


# In[5]:


mylist = [1,1,1,1,2,2,2,2,3,3,3,4]
s = set(mylist)
s


# In[6]:


len(s)


# In[7]:


print(1 in s)
print(5 in s)


# In[8]:


#seems like they are sorted however semantically they are not

set1 = {1,2,3,4}
set2 = {1,2,3,4,5}


# In[9]:


set1.issubset(set2)


# In[10]:


set2.issuperset(set1)


# In[11]:


set1 = {1,2,3}
set2 = {4,5,6}
set1.isdisjoint(set2)


# In[12]:


set1 = {1,2,3,4}
set2 = {1,2,3,4,5}
set3 = set1.union(set2)
set3


# In[13]:


set3 = set1.intersection(set2)
set3


# In[14]:


set3 = set2.difference(set1)


# In[15]:


set1 = {0,1,2,3,4}
set2 = {1,2,3,4,5}
set3 = set1.symmetric_difference(set2)
set4 = set1.difference(set2)
print(set3)
print(set4)


# In[16]:


set1.update(set2)
set1


# In[17]:


set1.remove(1)
print(set1)
set1.remove(42)


# In[ ]:


set1.discard(2)
print(set1)
set1.discard(42)


# In[ ]:


popped_out_element = set1.pop()
print(popped_out_element)


# In[ ]:


set1.clear()
set1

