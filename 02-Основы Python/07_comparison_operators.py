#!/usr/bin/env python
# coding: utf-8

# In[1]:


2 > 1


# In[2]:


result = 2 > 1
type(result)


# In[4]:


print(2 > 2)
print(2 >= 2)
print(3 >= 2)
print(3 >= 4)


# In[5]:


print(2 < 3)
print(3 < 2)
print(3 <= 3)
print(3 <= 2)
print(3 <= 4)


# In[6]:


1==1


# In[7]:


#1=1


# In[11]:


print("string" == "string")
print("string" == "another string")
print("String" == "string")
x = "String"
y = "string"
print(x.lower() == y.lower())


# In[45]:


#is


# In[46]:


1 != 1


# In[47]:


2 != 1


# Chaining

# In[48]:


1 < 2


# In[53]:


2 < 3


# In[50]:


1 < 2 < 3


# In[54]:


1 < 2 and 2 < 3


# In[55]:


1 > 2 and 2 < 3


# In[56]:


1 > 2 or 2 < 3


# In[57]:


1 > 2 or 2 > 3


# In[62]:


is_admin = True #prenend asking for security module
file_exists = True #pretend asking OS about file existance

should_open_file = is_admin and file_exists
should_open_file


# In[65]:


is_admin = False
if not is_admin:
    print('not an admin')
    
if is_admin==False:
    print("not an admin")


# In[ ]:




