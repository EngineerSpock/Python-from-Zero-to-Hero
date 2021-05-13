#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Character():
    #class object attribute
    #same for any instance of a class
    max_speed = 100
    dead_health = 0
    
    def __init__(self, race, damage = 10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100
        
    #Operations
    def hit(self, damage):
        self.health -= damage
        
    def is_dead(self):
        return self.health == Character.dead_health
    def set_speed(self, speed):
        global max_speed
        max_speed -= speed


# In[ ]:


unit = Character('Ork')
unit.max_speed #attributes are not called with ()


# In[ ]:


Character.max_speed


# In[ ]:


unit = Character('Ork')
unit.hit(20)
print(unit.health)


# In[ ]:


unit.set_speed(20)
unit.max_speed


# In[ ]:


unit.is_dead()


# In[ ]:


unit.hit(80)
unit.is_dead()

