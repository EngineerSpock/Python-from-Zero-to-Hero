#!/usr/bin/env python
# coding: utf-8

# In[ ]:


romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
def parse_roman(arabic):
    result = 0
    for i, c in enumerate(arabic):
        if i+1<len(arabic) and romans[arabic[i]] < romans[arabic[i+1]]:
            result-=romans[arabic[i]]
        else:
            result+=romans[arabic[i]]
    return result


# In[ ]:


print(parse_roman('I')==1)
print(parse_roman('II')==2)
print(parse_roman('IV')==4)
print(parse_roman('V')==5)
print(parse_roman('VI')==6)
print(parse_roman('IX')==9)
print(parse_roman('X')==10)
print(parse_roman('XIV')==14)
print(parse_roman('L')==50)
print(parse_roman('C')==100)
print(parse_roman('D')==500)
print(parse_roman('M')==1000)
print(parse_roman('XL')==40)
print(parse_roman('LX')==60)
print(parse_roman('XCIV')==94)

