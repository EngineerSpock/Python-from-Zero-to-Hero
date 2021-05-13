# 1
def whos_first(p1, p2):
	diff = p1.find('B') - p2.find('B')
	if diff < 0:
		return 'p1'
	elif diff > 0:
		return 'p2'
	else:
		return 'tie'
        
# 2
 def solve_hanoi_tower(discs):
    return 2**discs - 1
    
# 3
def calc_dice_scores(lst):
	return sum([a+b for a, b in lst]) if not any([a==b for a, b in lst]) else 0
    
# 4
def any_duplicates(square):
    plain = [i for x in square for i in x]
    return sorted(plain)!=[1,2,3,4,5,6,7,8,9]