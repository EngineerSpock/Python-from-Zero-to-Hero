#!/usr/bin/env python
# coding: utf-8

# In[10]:


numbers = [1,2,3,4,5]
for i in numbers:
    print(i)


# In[11]:


numbers = range(1, 6)
type(numbers)


# In[12]:


for i in numbers:
    print(i)


# In[13]:


for i in range(1, 6):
    print(i)


# In[15]:


for i in range(1, 6):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')


# In[20]:


numbers = [1,3,5,7,9]
for i, item in enumerate(numbers):
    numbers[i] *= 2
numbers


# In[21]:


name = "John"
for l in name:
    print(l)


# In[22]:


for _ in range(5):
    print('Alarm!')


# # For and Tuples

# In[24]:


person = ('John', 'Silver', 22)
for item in person:
    print(item)


# In[37]:


#many funcs return list of tuples
persons = [('John', 22), ('Bob', 32), ('Dave', 20)]
len(persons)


# In[38]:


#tuple unpacking
#for name, age in persons:
for (name, age) in persons:
    print(f'{name} is {age} years old')


# # For and Dict

# In[27]:


players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801, Ding=2797, Giri=2780)


# In[28]:


for item in players:
    print(item)


# In[29]:


for item in players.items():
    print(item)


# In[30]:


#tuple unpacking
for k,v in players.items():
    print(f'{k} has rating {v}')


# In[31]:


for v in players.values():
    print(v)


# In[36]:


#find all pairs sum of which equals 0
list1 = [2, 4, -5, 6, 8, -2,]
list2 = [2, -6, 8, 3, 5, -2,]

pairs = []
for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
pairs


# In[ ]:




