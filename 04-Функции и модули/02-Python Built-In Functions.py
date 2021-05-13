#!/usr/bin/env python
# coding: utf-8

# # Mathematical Functions

# In[ ]:


abs(-1)


# In[ ]:


max(1,2,3,4,5)


# In[ ]:


min([1,2,3,4,5])


# In[ ]:


pow(2,3)


# In[ ]:


round(3.37, 1)


# In[ ]:


sum([1,2,3,4])


# In[ ]:


h = hex(42)
o = oct(42)
b = bin(42)

print(h)
print(o)
print(b)


# # Functions on Iterables

# ## all(***iterable***) 

# In[ ]:


all_true1 = all([True, True, True])
all_true2 = all([True, False, True])

print(all_true1)
print(all_true2)


# In[ ]:


players = [('Carlsen', 2842), ('Caruana', 2822), 
          ('Mamedyarov', 2801), ('Ding', 2797),
          ('Giri', 2780)]


# In[ ]:


all(rating > 2700 for _, rating in players)


# In[ ]:


all(rating > 2800 for _, rating in players) #short-circuiting


# In[ ]:


all([rating > 2800 for _, rating in players]) 
#worse performance - no shortcircuting


# ## any(***iterable***)

# In[ ]:


any_true1 = all([False, False, True])
any_true2 = all([False, False, False])

print(all_true1)
print(all_true2)


# In[ ]:


players = [('Carlsen', 2842), ('Caruana', 2822), 
          ('Mamedyarov', 2801), ('Ding', 2797),
          ('Giri', 2780)]
any(rating < 2790 for _, rating in players)


# In[ ]:


any(rating < 2700 for _, rating in players)


# In[ ]:


letters = 'abcd'
numbers = (10, 20, 30)

join = zip(letters, numbers) #creates special iterator (lazy eval)
print(type(join))
print(join)

joined_list = list(join)
print(joined_list)


# In[ ]:


names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri']
ratings = [2842, 2822, 2801, 2797, 2780]

players = dict(zip(names, ratings))
players


# In[ ]:


reply = input()
reply


# In[ ]:


code = ord('a') #take Unicode code
code


# In[ ]:


c = chr(code)
c

