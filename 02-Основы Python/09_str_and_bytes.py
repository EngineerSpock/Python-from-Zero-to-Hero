#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
sys.getdefaultencoding()


# In[5]:


ord('a')


# In[6]:


chr(97)


# In[8]:


chr(198)


# In[12]:


s = 'hello'
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')

print(enc_ascii)
print(enc_utf8)
print(enc_utf16)


# In[14]:


print(len(enc_ascii))
print(len(enc_utf8))
print(len(enc_utf16))


# In[47]:


str_in_bytes = b'hello'
str_in_bytes = s.encode('utf8')

str_in_text = 'hello'

print(type(str_in_bytes))
print(type(str_in_text))


# In[55]:


print('bytes'.encode('utf-8'))
print('байты'.encode('utf-8'))


# In[53]:


print(str_in_bytes[0])
print(str_in_text[0])


# In[56]:


#str_in_bytes[0] = 'a'


# In[58]:


ba = bytearray(b'hello')
ba[0]=87
ba


# In[28]:


result = str(str_in_bytes)
print(result)
print(len(result))


# In[29]:


result = str(str_in_bytes, 'utf-8')
print(result)


# In[30]:


result = str_in_bytes.decode('utf-8')
print(result)


# In[45]:


jpeg = [120, 3, 255, 0, 100]
with open(r'C:\tmp\btest.bin', 'w+b') as file:
    file.write(bytes(jpeg))


# In[1]:


with open(r'C:\tmp\btest.bin', 'rb') as file:
    data = file.read()
    for b in data:
        print(int(b))    


# In[2]:


with open(r'C:\tmp\btest.bin', 'rb') as file:
    data = file.read()
    for b in data:
        print(b)    


# In[ ]:




