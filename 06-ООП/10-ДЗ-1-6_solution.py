#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1
class Name:

    def __init__(self, first_name, last_name):
        self.first_name = first_name.lower().capitalize()  # or first_name.title()
        self.last_name = last_name.lower().capitalize()  # or last_name.title()
        self.full_name = self.first_name + " " + self.last_name
        self.initials = self.first_name[0] + "." + self.last_name[0]


# In[2]:


# 2
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


# In[4]:


# 3
class Employee:
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    @classmethod
    def from_string(cls, str_to_parse):
        first_name, last_name, salary = str_to_parse.split('-')
        return cls(first_name, last_name, int(salary))


# In[5]:


# 4
class Pizza:
    order = 0
    def __init__(self,ingredients):
        self.ingredients = ingredients
        Pizza.order += 1
        self.order_number = Pizza.order
        
    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])


# In[6]:


# 5
import math
class Circle:
    def __init__(self, r=0):
        self.r = r

    def get_area(self):
        return math.pi * self.r ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.r


# In[7]:


# 6
prices = {"Strawberries" : 1.5, "Banana" : 0.5, "Mango" : 2.5,
        "Blueberries" : 1, "Raspberries" : 1, "Apple" : 1.75,
        "Pineapple" : 3.5}

class Beverage:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.price:.2f}'

    def get_name(self):
        lst = sorted([i.replace('ies','y') for i in self.ingredients])
        return f'{" ".join(lst)} {"Fusion" if len(lst)>1 else "Smoothie"}'

