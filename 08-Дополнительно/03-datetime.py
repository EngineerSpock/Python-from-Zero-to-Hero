#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta


# In[ ]:


d1 = date(2019, 3, 12)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)


# In[ ]:


t1 = time(23, 10, 59)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)


# In[ ]:


print(date.today())


# In[ ]:


print(date.max)
print(date.min)
print(time.max)
print(time.min)


# # datetime

# In[ ]:


dt = datetime(2019, 3, 12, 17, 15)
print(dt)


# In[ ]:


print(dt.date().year)
print(dt.time().hour)


# In[ ]:


print(datetime.max) 
print(datetime.min)


# In[ ]:


now = datetime.now()
print(now)


# In[ ]:


print(now.year)
print(now.month)
#etc with day, hour... 


# In[ ]:


new_dt = now.replace(year=2018)
print(new_dt)


# # parsing

# - %d: день месяца в виде числа
# - %m: порядковый номер месяца
# - %y: год в виде 2-х чисел
# - %Y: год в виде 4-х чисел
# - %H: час в 24-х часовом формате
# - %M: минута
# - %S: секунда

# In[ ]:


dt = datetime.strptime("30/08/2018", "%d/%m/%Y")
print(dt)
 
dt = datetime.strptime("29/03/2018 10:40", "%d/%m/%Y %H:%M")
print(dt)     
 
dt = datetime.strptime("06-28-2018 09:20", "%m-%d-%Y %H:%M")
print(dt)     

dt = datetime.strptime('2018-06-28', '%Y-%m-%d')
print(dt)


# # formatting

# - %a: аббревиатура дня недели. Например, Wed - от слова Wednesday (по умолчанию используются английские наименования)
# - %A: день недели полностью, например, Wednesday
# - %b: аббревиатура названия месяца. Например, Oct (сокращение от October)
# - %B: название месяца полностью, например, October
# - %d: день месяца, дополненный нулем, например, 01
# - %m: номер месяца, дополненный нулем, например, 05
# - %y: год в виде 2-х чисел
# - %Y: год в виде 4-х чисел
# - %H: час в 24-х часовом формате, например, 13
# - %I: час в 12-ти часовом формате, например, 01
# - %M: минута
# - %S: секунда
# - %f: микросекунда
# - %p: указатель AM/PM
# - %c: дата и время, отформатированные под текущую локаль
# - %x: дата, отформатированная под текущую локаль
# - %X: время, форматированное под текущую локаль

# In[ ]:


import locale
locale.setlocale(locale.LC_ALL, "")


# In[ ]:


now = datetime.now()
print(now.strftime('%Y-%m-%d (%a)'))
print(now.strftime('%Y %B %d число (%A)'))


# # timedelta

# In[ ]:


from datetime import timedelta


# In[ ]:


delta1 = timedelta(days=3, hours=2, minutes=10)
print(delta1)


# In[ ]:


delta2 = timedelta(days=2, hours=1, minutes=5)


# In[ ]:


print(delta1 - delta2)
print(delta2 - delta1)


# In[ ]:


my_bithday = date(1988, 8, 12)

delta = date.today() - my_bithday
print(type(delta))

my_age = int(delta.days / 365)
print(my_age)


# In[ ]:


wife_birthday = date(1990, 9, 6)

am_i_older = my_bithday < wife_birthday
print(am_i_older)

