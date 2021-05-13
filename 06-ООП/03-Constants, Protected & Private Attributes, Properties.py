#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Character():
    MAX_SPEED = 100
    
    def __init__(self, race, damage = 10):
        self.damage = damage
        
        self.__race = race
        self._health = 100
        
        self._current_speed = 20
        
    def hit(self, damage):
        self._health -= damage
        
    @property
    def health(self):
        return self._health
    
    @property
    def race(self):
        return self.__race
    
    @property
    def current_speed(self):
        return self._current_speed
    
    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed                


# In[ ]:


Character.MAX_SPEED


# In[ ]:


Character.MAX_SPEED = 10
Character.MAX_SPEED


# In[ ]:


c = Character('Elf')


# In[ ]:


c.__race


# In[ ]:


c._Character__race = 'Ork'
c._Character__race


# In[ ]:


c._health = 0
c._health


# In[ ]:


print(c.health)
print(c.race)


# In[ ]:


c.health = 10


# In[ ]:


c.current_speed


# In[ ]:


c.current_speed = 50
c.current_speed


# In[ ]:


c.current_speed = 1000
c.current_speed


# In[ ]:


c.current_speed = -10
c.current_speed

