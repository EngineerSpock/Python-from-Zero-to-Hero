#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'

d3 = {}
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'


# In[2]:


print(d1==d2)
print(d1==d3)


# In[3]:


for k, v in d1.items():
    print(k, v)


# In[4]:


from collections import OrderedDict


# In[5]:


d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
d2['c'] = 'C'

d3 = OrderedDict()
d3['a'] = 'A'
d3['b'] = 'B'
d3['c'] = 'C'


# In[6]:


print(d1==d2)
print(d1==d3)


# In[7]:


for k, v in d1.items():
    print(k, v)


# In[ ]:




