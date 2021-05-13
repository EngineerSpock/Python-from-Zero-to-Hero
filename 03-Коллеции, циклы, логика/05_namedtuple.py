#!/usr/bin/env python
# coding: utf-8

# In[12]:


players = [('Carlsen', 1990, 2842), ('Caruana', 1992, 2822), ('Mamedyarov', 1985, 2801)]
print(players[0])
#print(players[0].name)


# In[2]:


from collections import namedtuple


# In[3]:


Player = namedtuple('Player', 'name age rating')


# In[13]:


players = [Player('Carlsen', 1990, 2842), Player('Caruana', 1992, 2822), Player('Mamedyarov', 1985, 2801)]


# In[14]:


players[0]


# In[15]:


players[0].name


# In[16]:


p1 = Player('Carlsen', 1990, 2842)
print(p1.name)
print(p1.age)
print(p1.rating)


# In[ ]:




