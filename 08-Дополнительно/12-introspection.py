#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print (issubclass.__doc__)


# In[ ]:


help(issubclass)


# In[ ]:


class Shape:
    pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

circle = Circle(10)


# In[ ]:


print(issubclass(Circle, Shape))


# In[ ]:


print(isinstance(circle, Circle))
print(isinstance(circle, Shape))


# In[ ]:


isinstance(circle, Shape)


# In[ ]:


print(isinstance(12, int))
print(isinstance("hi", str))

print(isinstance("hi", float))


# In[ ]:


print(callable(circle)) # objects that define __call__() are considered callable
print(callable(print))


# In[ ]:


if hasattr(circle, 'radius'):
    print(getattr(circle, 'radius'))
    setattr(circle, 'radius', 20)
    print(getattr(circle, 'radius'))


# In[ ]:


dir(circle) # смотрим атрибуты


# In[ ]:


Circle.__name__


# In[ ]:


__name__


# In[ ]:


type(circle)


# In[ ]:


circle2 = circle


# In[ ]:


print(id(circle))
print(id(circle2))


# In[ ]:


repr(circle)

