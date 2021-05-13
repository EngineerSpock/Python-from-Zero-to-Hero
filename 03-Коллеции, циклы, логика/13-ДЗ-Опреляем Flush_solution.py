table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_C"]

# ниже ваша реализация:
suites = 'CHSD'
flush = False

table_suites = [i[-1] for i in table_cards]
hand_suites = [i[-1] for i in hand_cards]
suites_in_game = table_suites + hand_suites

# and either with a list comprehension:
flush = any([suites_in_game.count(suit) >= 5 for suit in suites])
if flush:
    print('Flush!')
else:
    print('No Flush!')
    
 # or more procedural
 flush = False
 for suit in suites:
    if suites_in_game.count(suit) >= 5:
        flush = True
 
 if flush:
    print('Flush!')
 else:
    print('No Flush!')