#!/usr/bin/env python
# coding: utf-8

# In[1]:


if True:
    print('Indeed, true.')


# In[2]:


if 3 > 2:
    print('3 is greater than 2')


# In[3]:


is_admin = True
#is_admin = False
if is_admin:
    print("It's admin, look at him!")


# In[6]:


is_admin = True
if is_admin:
#if is_admin == True:
    print("It's admin, look at him!")
else:
    print("No, that's not an admin!")


# In[10]:


selected_character = input()

if selected_character == 'Protos':
    print('Protos is the most powerful race')
elif selected_character == 'Zerg':
    print('Zerg is the most weak race but it spreads like a plague')
elif selected_character == 'Terrain':
    print('Terrain is a race balanced between zerg and protos')
else:
    print('Hmm... it seems we have a new race')


# In[ ]:




