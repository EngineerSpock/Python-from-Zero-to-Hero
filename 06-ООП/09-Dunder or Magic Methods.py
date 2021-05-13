#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# In[ ]:


class Road():
    def __init__(self, length):
        self.length = length        
        
    #def __len__(self):
    #    return self.length
    
    #def __str__(self):
    #    return f'A road of length:{self.length}'
    
    #def __del__(self):
    #   print f'The road has been destroyed.'


# In[ ]:


r = Road(100)


# In[ ]:


len(r)


# In[ ]:


print(r)


# In[ ]:


str(r)


# In[ ]:


#__del__, __add__, __repr__ and others exist and all of them can be overriden

