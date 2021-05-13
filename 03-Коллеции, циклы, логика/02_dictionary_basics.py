#!/usr/bin/env python
# coding: utf-8

# In[1]:


players = {
             'Carlsen' : 2842, 
             'Caruana' : 2822, 
             'Mamedyarov' : 2801,
             'Ding' : 2797,
             'Giri' : 2780,
          }
players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801, Ding=2797, Giri=2780)
players


# In[2]:


top1 = players['Carlsen']
print(f"Top chess player's rating is {top1}")


# In[3]:


players.get('Carlsen')


# In[4]:


players['So'] = 2780 #add
players


# In[5]:


players['So'] = 2781 #update
players


# In[6]:


del players['So']
players


# In[7]:


l = list(players.keys())
type(l)


# In[8]:


k = players.keys()
type(k)


# In[9]:


sorted(players.keys())


# In[10]:


print('Carlsen' in players)
print('Kramnik' not in players)


# In[11]:


vals = list(players.values())
type(vals)


# In[12]:


vals = players.values()
type(vals)


# In[13]:


sorted(players.values())


# In[14]:


players_copy = players.copy()
print(players_copy)


# In[15]:


for k, v in players.items():
    print(k, v)


# In[16]:


players.pop('Giri')
print(players)


# In[17]:


print(players.popitem())
print(players)


# In[19]:


len(players)


# In[20]:


players.setdefault('Karjakin')
players


# In[ ]:




