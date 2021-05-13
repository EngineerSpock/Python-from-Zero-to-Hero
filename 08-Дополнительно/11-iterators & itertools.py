#!/usr/bin/env python
# coding: utf-8

# Есть маленькая тонкость: следует различать понятия объекта-итератора и итерируемого объекта. Итератор это объект который используется для итерации по итериуемому объекту, используя __next__() dunder-метод.
# 
# Справедливо следующее утверждение: любой объект-итератор итерируем, но не любой итерируемый объект является объектом-итератором. Например, list итерируем, но само по себе итератором не является. Чтобы получить итератор из итерируемого объекта, надо воспользоваться методом __iter__(), который, собственно, и возвращает объект-итератор.
# 
# Создадим итерируемый объект типа list:

# In[ ]:


iterable = [1, 2, 3]

# получим объект-итератор
iterator = iter(iterable) # будет вызван метод __iter__() реализованный списком
print(type(iterator))

# а теперь пройдёмся по итератору с помощью next():
print(next(iterator)) # будет вызван метод __next__() реализованный внутри объекта-итератора

#повторим, пройдясь до конца:
print(next(iterator))
print(next(iterator))


# itertools - это модуль стандартной библиотеки, который содержит множество продвинутых функций для работы с итераторами.
# 
# Этот модуль в том числе позволяет строить сложные итераторы, посредством их комбинирования. По сути, itertools реализует так называемую "алгебру итераторов", а вдохновлением этой концепции послужили идеи из таких функциональных языков как Haskell, APL и SML. Все функции предполагают ленивое выполнение, что позволяет экономить память и работать с последовательностями наиболее эффективно.
# 
# Условно, функции можно разделить на три группы: 
# 
# - бесконечные итераторы
# - итераторы, завершающие исполнение по наикратчайшей входной последовательности
# - комбинаторные итераторы

# In[ ]:


# прежде чем использовать функции itertools, надо импортировать модуль
import itertools as it


# # Бесконечные итераторы

# ## count()
# Сгенерируем чётные числа. Это можно сделать с помощью list comprehensions:

# In[ ]:


even_numbers = [x for x in range(10) if x % 2 == 0 ]
print(even_numbers)


# при этом результаты сразу материализуются (память выделяется под все сгенерированные элементы).
# 
# Можно сделать тоже самое, но с ленивым исполнением:

# In[ ]:


even_numbers = it.count(0, 2) # 0 - начальное значение, 2 - шаг
even_numbers


# count() возвращает бесконечный итератор и тут есть ловушка: если мы просто пойдём циклом по итератору, то никогда из него не выйдем

# In[ ]:


# for x in even_numbers:
#     print(x)


# можно было бы внутри цикла сделать break по условию, но это было бы не очень красиво (не "питонический" путь).
# Эффектней скомбинировать с list comprehension:

# In[ ]:


list(next(even_numbers) for _ in range(5))


# Здесь мы материализуем все элементы, однако делаем это отложенно (после конструирования итератора), что даёт гибкость с точки зрения возможностей комбинирования итераторов. Например, мы можем сэмулировать работу встроенной функции enumerate():

# In[ ]:


list(zip(it.count(), ['a', 'b', 'c'])) #zip - встроенная функция, строящая итератор (она не из iterools, но какая разница!)


# Не правда ли круто? Это дало возможность проитерировать по списку, не используя for, и, не зная длину этого самого списка.
# Это не говоря о том, что без механизма ленивого исполнения мы практически не в состоянии эффективно решить задачу, когда необходимо генерировать гигантское количество элементов до тех пор пока не решим **в рантайме (время исполнения программы) остановить генерацию.**

# ## repeat и cycle

# Иногда нам нужно сгенерировать последовательность из повторяющихся элементов. repeat в этом поможет:

# In[ ]:


def print_iterable(iterable, end = None):
    for x in iterable:
        if end:
            print(x, end=end)
        else:
            print(x)            


# In[ ]:


ones = it.repeat(1, 5) # позволяет задать значение, которое повторяется и кол-во повторов
print_iterable(ones, ' ')


# Зачастую, repeat используется для генерации потока состоящего из одной константы, для использования в map и zip.
# Например, можно весьма эффектно сгенерировать последовательность квадратов натуральных чисел:

# In[ ]:


list(map(pow, range(10), it.repeat(2)))


# При организации цикла с очень большом количеством итераций, repeat будет работать быстрее чем range:

# In[ ]:


for _ in itertools.repeat(None, 10000):
    # compute()
    
# range медленнее:
for _ in range(10000):
    # compute()


# repeat в данном случае будет просто управлять счётчиком объекта None, в то время как range будет генерировать массу целых чисел (а это работат медленнее). Если речь идёт о десятке другом итераций, то можно вполне обойтись и стандартным подходом с range.

# Если мы хотим создать бесконечный итератор по набору значений, то можем использовать cycle():

# In[ ]:


pos_neg_ones = it.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(10)))

letters = it.cycle(['A', 'B', 'C'])
print(list(next(letters) for _ in range(10)))


# # Iterators terminating on the shortest input sequence

# # accumulate

# accumulate без параметров генерирует последовательность как бы "нарастающим итогом":

# In[ ]:


list(it.accumulate([1, 2, 3, 4, 5]))


# In[ ]:


list(it.accumulate(['A', 'B', 'C', 'D']))


# Вся мощь accumulate заключена в том, что вы можете накладывать любую функцию, которая принимает два элемента и продуцирует результат по какому-либо принципу:

# In[ ]:


list(it.accumulate([3, 1, 4, 2, 7, 3, 8, 5, 9], max))


# Первым элементом выходной последовательности всегда является первый же элемент входной последовательности. Даже если бы мы передали min вместо max, всё равно первым элементом в результате была бы тройка.
# 
# Фактически, далее accumulate берёт два элемента и применяет к ним переданную функцию. max определяет, что 3 > 1 и возвращает 3, затем:
# 
# - 4 > 3
# - 4 > 2
# - 7 > 4
# - 7 > 3
# - 8 > 7
# - 8 > 5
# - 9 > 8
# 
# Разумеется, никто нам не запрещает передать полновесную кастомную (собственную) функцию или лямбда-выражение в accumulate.

# ## chain & chain.from_iterable

# In[ ]:


list(it.chain('ABC', 'DEF'))


# In[ ]:


list(it.chain.from_iterable(['ABC', 'DEF'])) # "раскладывает" один список; не принимает более одного списка


# In[ ]:


list(it.chain([1, 2, 3], [4, 5, 6], [7, 8, 9]))


# ## takewhile & dropwhile & filterfalse

# In[ ]:


list(it.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5]))


# In[ ]:


list(it.takewhile(lambda x: x < 3, [1, 2, 3, 4, 5]))


# In[ ]:


list(it.filterfalse(lambda x: x % 2 == 0, range(10)))


# ## tee

# tee возвращает n итераторов для входящей последовательности. Напомню, что по итератору можно пройтись только один раз:

# In[ ]:


iterable = iter([1, 2, 3])
print_iterable(iterable, ' ')
print('\niterable is exhausted')
print_iterable(iterable, ' ') # empty output


# Если мы хотим более одного раза получить итератор, то можно использовать tee():

# In[ ]:


iterable1, iterable2 = it.tee([1, 2, 3], 2)
print_iterable(iterable1, ' ')
print('\niterable is exhausted')
print_iterable(iterable2, ' ')


# ## zip vs zip_longest

# In[ ]:


names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri']
ratings = [2842, 2822, 2801, 2797, 2780]

for name, rating in zip(names, ratings):
    print(f'{name}:{rating}')


# In[ ]:


list(zip(names, ratings))


# In[ ]:


players = dict(zip(names, ratings))
players


# In[ ]:


# different length
names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri', 'Kramnik']
ratings = [2842, 2822, 2801, 2797, 2780]

players = dict(zip(names, ratings))
players


# In[ ]:


players = dict(it.zip_longest(names, ratings))
players


# In[ ]:


players = dict(it.zip_longest(names, ratings, fillvalue = 0))
players


# In[ ]:


from platform import python_version

print(python_version())


# ## groupby

# groupby возвращает итератор по кортежам (tuples) первый элемент в которых - ключи, а второй элемент - итератор по сгруппированным данным.
# Если мы не передаём ключ для группировки, то группировка будет происходить непосредственно по элементам коллекции, например:  

# In[ ]:


for key, grp in it.groupby([1, 1, 1, 2, 2, 2, 3, 3]):
    print('{}: {}'.format(key, list(grp)))


# groupby, на самом деле, имеет довольно странное поведение:

# In[ ]:


for key, grp in it.groupby([1, 2, 1, 2, 2, 3, 3, 2]):
    print('{}: {}'.format(key, list(grp))) 


# На этом примере видно, что groupby учитывает порядок следования элементов. Эта функция группирует только последовательно стоящие идентичные ключи. Чтобы этого избежать, необходимо заранее отсортировать последовательность по ключу по которому мы собираемся далее осуществить группировку. В данном случае, мы имеет дело с обыкновенными целыми числами, так что можно просто воспользоваться функцией sorted:

# In[ ]:


lst = [1, 2, 1, 2, 2, 3, 3, 2]
for key, grp in it.groupby(sorted(lst)):
    print('{}: {}'.format(key, list(grp))) 


# In[ ]:


forecast = [ { 'humidity' :  20, 'temperature' : 78, 'wind' :  7} ,
             { 'humidity' :  50, 'temperature' : 61, 'wind' : 10} ,
             { 'humidity' : 100, 'temperature' : 81, 'wind' :  5} ,
             { 'humidity' :  90, 'temperature' : 62, 'wind' : 15} ,
             { 'humidity' :  20, 'temperature' : 84, 'wind' : 19} ,
             { 'humidity' :   0, 'temperature' : 66, 'wind' : 28} ,
             { 'humidity' :   100, 'temperature' : 87, 'wind' : 12} ,
             { 'humidity' :   0, 'temperature' : 68, 'wind' : 14} ,
             { 'humidity' :   90, 'temperature' : 86, 'wind' :  4} ,
             { 'humidity' :  50, 'temperature' : 68, 'wind' :  0}
           ] 


# In[ ]:


def group_sorted(iterable, key=None):
    """Group sorted `iterable` on `key`."""
    return it.groupby(sorted(iterable, key=key), key=key)


# In[ ]:


grouped_data = group_sorted(forecast, key=lambda x: x['humidity'])
for key, grp in grouped_data:
    print('{}: {}'.format(key, list(grp)))


# ## islice

# islice - очень полезная функция, которая даёт возможность, например, из бесконечного итератора взять строго определённое кол-во элементов. Может принимать четыре аргумента: итерируемый объект, индекса начала и конца и шаг. 

# In[ ]:


even_numbers = it.count(0, 2)
print([x for x in range(20) if x % 2 == 0])

print(list(it.islice(even_numbers, 2, 10, 2)))


# In[ ]:


even_numbers = it.count(0, 2)
print(list(it.islice(even_numbers, 4)))


# In[ ]:


even_numbers = it.count(0, 2)
print(list(it.islice(even_numbers, 2, 4)))


# # Combinatoric iterators

# In[ ]:


# предположим, что мы помним, что наш пин состоит из 7, 5, 2, 8, но последовательность не помним.
# выведем все возможные варианты

pin = [7, 5, 2, 8]


# In[ ]:


list(it.permutations(pin))


# In[ ]:


# давайте эффектно сгенерируем колоду карт

ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', ]
suits = ['H', 'D', 'C', 'S']

lst = list(it.product(ranks, suits))
lst


# In[ ]:


list(it.combinations(lst, 2))


# In[ ]:


list(it.combinations('ABCD', 2))

