#!/usr/bin/env python
# coding: utf-8

# Mixin is the special case of multiple inheritance. No special syntax for that is required, they are special only from the semantics point of view.
# 
# - это независимые классы от которых можно наследоваться, но их не надо, например, инициализировать, поскольку они полностью независимы и функционалом, который они предоставляют можно просто брать и пользоваться (как правило)
# - миксины не создаются как базовый класс предназначенный для конкретной иерархии, его можно примешивать в любой класс

# In[ ]:


class Vehicle:
    """A generic vehicle class."""

    def __init__(self, position):
        print("create vehicle)")
        self.position = position
        
    def travel(self, destination):
        route = calculate_route(source=self.position, to=destination)
        self.move_along(route)

    def calculate_route(self, source, to):
        return 0
    
    def move_along(self, route):
        print('moving')
        
class Car(Vehicle):
    pass

class Airplane(Vehicle):
    pass


# Как подключить функционал радио к машине так, чтобы не добавить его к самолёту?
# Можно использовать mixin:

# In[ ]:


class RadioMixin:
    def __init__(self):
        print("create radio")
        self.radio = Radio()

    def turn_on(self, station):
        self.radio.set_station(station)
        self.radio.play()
        
class Radio:
    def set_station(self, station):
        self.station = station
        
    def play(self):
        print(f"Playing {self.station}")
        
class Car(Vehicle, RadioMixin):    
    def __init__(self):
        #super(Vehicle, self).__init__(10)
        #super(RadioMixin, self).__init__()
        #Vehicle.__init__(self, (10,20))
        #RadioMixin.__init__(self)


# In[ ]:


car = Car()
car.turn_on("Moscow FM")


# In[ ]:


# хороший пример из книги "Effective Python: 59 Specific Ways to Write Better Python"
class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
            
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value
        
class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# In[ ]:


tree = BinaryTree(10,
    left=BinaryTree(7, right=BinaryTree(9)),
    right=BinaryTree(13, left=BinaryTree(11)))
print(tree.to_dict())


# хорошо то, что поведение миксинов может быть и переопределено, ничто не мешает. если несколько классов наследуют один и тот же миксин, они могут быть использованы полиморфно и в каком-то случае будет вызвана реализация примешенного функционала по умолчанию, а в каком-то переопределённая наследником
# 
