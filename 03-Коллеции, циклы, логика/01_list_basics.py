#!/usr/bin/env python
# coding: utf-8

# In[1]:


int_list = [1,2,3]


# In[2]:


mixed_list = [1, 2.0, 'string']


# In[3]:


len(int_list)


# In[4]:


print(int_list[0])
print(int_list[-1])


# In[5]:


int_list[1:]


# In[6]:


names1 = ['John', 'Bob', 'Alice']
names2 = ['Tracy', 'Elijah', 'Mason']

names1 + names2


# In[7]:


names1[0] = 'Liam'
names1


# In[8]:


names1.append('William')
names1.append('James')
names1


# In[9]:


popped = names1.pop() #same as names1.pop(-1)
print(popped)
print(names1)


# In[10]:


names1.pop(0)
names1


# In[11]:


names1.append('James')
names1.sort()
names1


# In[21]:


letters = ['ac', 'ab', 'aa']
letters.sort()
print(letters)

letters = ['abc', 'a', 'ab']
letters.sort(key=len)
print(letters)


# In[23]:


letters = ['ac', 'ab', 'aa']
result = sorted(letters)
print(type(result))
print(result)


# In[1]:


numbers = [3,2,8,5,0,3,4,1]
print(numbers)
numbers.sort() #actually it is Timsort
print(numbers)


# In[14]:


numbers = [3,2,8,5,0,3,4,1]
numbers.reverse()
numbers


# In[15]:


numbers.sort(reverse=True)
numbers


# In[16]:


numbers.insert(0, 22)
numbers


# In[2]:


print(numbers.index(42))


# In[ ]:


print(numbers.count(3))


# In[ ]:


copy = numbers.copy()
print(copy)


# In[ ]:


numbers.clear()
numbers

