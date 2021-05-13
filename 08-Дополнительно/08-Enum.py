#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from enum import Enum


# In[ ]:


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


# In[ ]:


TrafficLight.RED


# In[ ]:


print(TrafficLight.RED)


# In[ ]:


print(TrafficLight.RED.name)
print(TrafficLight.RED.value)


# In[ ]:


for c in TrafficLight:
    print(c)


# In[ ]:


TrafficLight(1)


# In[ ]:


TrafficLight['RED']


# In[ ]:


print(TrafficLight.RED == TrafficLight.RED)
print(TrafficLight.GREEN == TrafficLight.RED)


# In[ ]:


from enum import IntEnum


# In[ ]:


class Priority(IntEnum):
    LOW = 1
    NORMAL = 2
    HIGH = 3


# In[ ]:


Priority.LOW < Priority.NORMAL


# In[ ]:


from enum import IntFlag


# In[ ]:


class Color(IntFlag):
    RED = 1
    GREEN = 2
    BLUE = 4


# In[ ]:


combination = Color.RED | Color.GREEN
combination


# In[ ]:


Color.RED in combination


# In[ ]:


get_ipython().set_next_input('bool(Color.RED & Color.GREEN) - show or not');get_ipython().run_line_magic('pinfo', 'not')


# In[ ]:


get_ipython().set_next_input('bool(Color.RED | Color.GREEN) - show or not');get_ipython().run_line_magic('pinfo', 'not')


# In[ ]:


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)
    JUPITER = (1.9e+27,   7.1492e7)
    SATURN  = (5.688e+26, 6.0268e7)
    URANUS  = (8.686e+25, 2.5559e7)
    NEPTUNE = (1.024e+26, 2.4746e7)
    def __init__(self, mass, radius):
        self.mass = mass       # in kilograms
        self.radius = radius   # in meters
    @property
    def surface_gravity(self):
        # universal gravitational constant  (m3 kg-1 s-2)
        G = 6.67300E-11
        return G * self.mass / (self.radius * self.radius)

Planet.EARTH.value
(5.976e+24, 6378140.0)
Planet.EARTH.surface_gravity
9.802652743337129

