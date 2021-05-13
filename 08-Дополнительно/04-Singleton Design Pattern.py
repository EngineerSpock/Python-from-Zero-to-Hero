#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Character:
    
    def __init__(self):
        self.race = "Elf"


# In[ ]:


c = Character()
c.race


# In[ ]:


class Character:
    
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)    
        return cls._instance
    
    def __init__(self):
        self.race = "Elf"


# In[ ]:


c = Character()
c.race


# In[ ]:


d = Character()
d.race = "Ork"


# In[ ]:


print(c.race)
print(d.race)

