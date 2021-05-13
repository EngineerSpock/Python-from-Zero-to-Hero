#!/usr/bin/env python
# coding: utf-8

# Len and Count

# In[6]:


x="hello, my name is Elias"


# In[7]:


len(x)


# In[8]:


x[len(x)-1]


# In[9]:


x.count('l')


# Casing

# In[10]:


x.capitalize()


# In[14]:


upper_cased=x.upper()
print(upper_cased)


# In[18]:


lower_cased=upper_cased.lower()
print(lower_cased)


# In[22]:


print(upper_cased.isupper())
print(lower_cased.islower())
print(x.isupper())
print(x.islower())


# In[32]:


print(x.find('l'))
print(x.find('l', 5))
print(x.find('l', 5, 10))
print(x.find('m', 7, 15))
print(x.find('m', 8, 15))


# Is Functions

# In[35]:


print('123abc'.isalnum())
print('123abc!'.isalnum())


# In[36]:


print('123abc'.isalpha())
print('abc'.isalpha())


# Checking on emptyness

# In[43]:


print(" ".isspace())
print("".isspace())


# In[44]:


print("" == "")
print("   ".strip(' ') == "")


# In[55]:


s = ""
if not s:
    print("empty string")


# In[48]:


h = "hello"
print(h.startswith("he"))
print(h.endswith("lo"))


# Splitting and Partitioning

# In[60]:


split = h.split('l')
print(type(split))
print(split)
split = h.split('e')
print(split)


# In[61]:


sentence = "12;10;8;10"
sentence.split(';')


# In[62]:


string = "Python is fun"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('not '))

string = "Python is fun, isn't it"

# splits at first occurence of 'is'
print(string.partition('is'))


# In[ ]:




