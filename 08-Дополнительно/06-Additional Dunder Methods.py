#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lst = [1, 2, 3]


# In[ ]:


repr(lst)


# In[ ]:


print(lst)


# In[ ]:


eval(repr(lst)) == lst


# In[ ]:


from datetime import datetime

dt = datetime.now()


# In[ ]:


repr(dt)


# In[ ]:


print(dt)


# In[ ]:


class Character():
    
    def __init__(self, race, damage = 100):
        self.race = race
        self.damage = damage
        
    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"
    
    def __str__(self):
        return f"{self.race} with damage = {self.damage}"
    
    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False
    
    # def __ne__(self, other):
    #     pass


# In[ ]:


c = Character("Elf")
print(c)


# In[ ]:


d = eval(repr(c))
type(d)


# In[ ]:


print(d)


# In[ ]:


c == d


# In[ ]:


# c!=d

