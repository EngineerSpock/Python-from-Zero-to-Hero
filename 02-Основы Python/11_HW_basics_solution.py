# 1 
prompt = input('Enter the number of cups')
cups = int(prompt)
free_cups = int(cups / 6)
print(free_cups)

# or even shorter
cups = int(input('Enter the number of cups'))
print(int(cups / 6))

# 2
x1 = int(input('Enter x1'))
y1 = int(input('Enter y1'))
x2 = int(input('Enter x2'))
y2 = int(input('Enter y2'))

distance = round(((x1-x2)**2+(y1-y2)**2)**0.5, 3)
print(distance)

# 3
chicken = int(input('How many chicken?'))
cows = int(input('How many cows?'))
pigs = int(input('How many pigs?'))

total_legs = chicken * 2 + (cows + pigs) * 4
print(total_legs)