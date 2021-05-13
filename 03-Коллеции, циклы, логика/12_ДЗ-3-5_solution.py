# 1
limit = int(input('Enter the limit'))

total_sum = 0
for x in range(limit + 1):
	if x % 3 == 0 or x % 5 == 0:
		total_sum += x
	else:
		continue

print(f'Total sum = {total_sum}')

# or using a list comprehension
limit = int(input('Enter the limit'))

total_sum = sum([x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0])

# 2
first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

joined_list = []
for x in first_list:
    if x % 2 != 0:
        joined_list.append(x)
        
for x in second_list:
    if x % 2 == 0:
        joined_list.append(x)
       
print(f'Merged list: {joined_list}')

#or using list comprehensions
first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]

odds = [x for x in first_list if x % 2 != 0]
evens = [x for x in second_list if x % 2 == 0]
joined_list = odds + evens

print(f'Merged list: {joined_list}')

# 3
current_hand = [2, 3, 4, 10, 'Q', 5]

cards = {2:1, 3:1, 4:1, 5:1, 6:1, 7:0, 8:0, 9:0, 10:-1, 'J':-1, 'Q':-1, 'K':-1, 'A':-1}

cards_sum = sum([cards[x] for x in current_hand])
print(cards_sum)