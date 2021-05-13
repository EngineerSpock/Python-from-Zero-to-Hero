#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Character():
    
    def __init__(self, race, armor, damage = 10):
        self.race = race        
        self.damage = damage
        self.armor = armor
        self.health = 100
        
    def hit(self, damage):
        self.health -= damage
        
    def is_dead(self):
        return self.health == 0
    
    #def __getstate__(self):        
    
    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)


# In[ ]:


c = Character('Elf')
c.hit(10)
c.health


# In[ ]:


import pickle
with open(r'C:\tmp\game_state1.bin', 'w+b') as f:
    pickle.dump(c, f)


# In[ ]:


c = None
print(c)


# In[ ]:


with open(r'C:\tmp\game_state1.bin', 'rb') as f:
    c = pickle.load(f)

print(c.health)


# In[ ]:


print(c.__dict__)

