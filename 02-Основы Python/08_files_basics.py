#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# Open

# In[2]:


# %%writefile is a short command for writing data to a file in Jupyter 
# (don't do that in PyCharm or other IDEs)

%%writefile sample.txt
Name|Phone
John;1234
Bob;5678
Alice;9432


# In[3]:


file = open('sample.txt')


# In[4]:


file


# Read

# In[5]:


data = file.read()


# In[6]:


data


# In[7]:


print(data)


# In[8]:


file.read()


# In[9]:


file.seek(0)
file.read()


# In[10]:


file.seek(0)


# In[11]:


lines = file.readlines()
print(type(lines))
print(lines)


# In[12]:


#file = open('C:\Users\EngineerSpock\JupyterRoot\sample.txt')
sample_file = open(r'C:\Users\EngineerSpock\JupyterRoot\sample.txt')

#or open with double back slashes: file = open('C:\\Users\\EngineerSpock\\JupyterRoot\\sample.txt')
#on Linux, we use slashes, so there's no need in r'
#file = open(/Users/EngineerSpock/JupyterRoot/sample.txt')


# Close

# In[13]:


file.close()
sample_file.close()

print(file.closed)
print(sample_file.closed)


# In[7]:


with open('sample.txt') as sample_file:
    sample_data = sample_file.read()
    print(sample_file.closed)
print(sample_file.closed)


# In[4]:


print(sample_data)


# # File Modes
# 
# * **mode='r'** - read only (error if writing)
# * **mode='w'** - write only (error if reading, overwrites existing file or creates new one)
# * **mode='a'** - append only (error if reading or writing to inexistent file)
# * **mode='r+'** - reading and writing (error if writing to inexistent file)
# * **mode='w+'** - reading and writing (overwrites existing file or creates new one)
# 
# *trying to read an inexistent file always leads to an error*

# In[16]:


#with open('sample.txt', mode='w') as sample_file:
#    data = sample_file.read()


# In[17]:


with open('sample.txt', mode='a') as sample_file:
    sample_file.write('Eric;7639')


# In[18]:


with open('sample.txt', mode='r') as sample_file:
    print(sample_file.read())


# In[19]:


#how to read and append?
with open('sample.txt', mode='r+') as sample_file:
    sample_file.seek(0, 2)
    sample_file.write('\nToub;5627')
    sample_file.seek(0)
    print(sample_file.read())


# In[20]:


with open('abracadabra.txt', mode='w+') as spell_file:
    spell_file.write('abra-abra-abra-cadabra')
    spell_file.seek(0)
    print(spell_file.read())


# In[ ]:




