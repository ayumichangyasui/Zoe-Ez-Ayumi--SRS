def bananabid(my_player_number, my_bananas, monkey_position, opponent_bananas, past_bid_list, turn_number):
    #opponent broke --> bid 1
    if opponent_bananas == 0:
        return 1

    # just in case, so it doesn't crash!!! game over
    if abs(monkey_position)>= 3:
        return 0

#are we abt to win? --> go all in
    gna_win = (my_player_number== 1 and monkey_position == -2) or (my_player_number == 2 and monkey_position == 2)
    if gna_win:
        return my_bananas

#og strats
    if opponent_bananas> 150:
        standard_bid = my_bananas// 8
    elif opponent_bananas >100:
        standard_bid = my_bananas //6
    elif opponent_bananas > 50:
        standard_bid = my_bananas// 4
    else:
        standard_bid = my_bananas //3

#ohno we're losing, bid more (multiplier)
    if (my_player_number == 1 and monkey_position > 0) or (my_player_number == 2 and monkey_position < 0):
        multiplier =1.5 
    if (my_player_number == 1 and monkey_position > 0) or (my_player_number == 2 and monkey_position < 0):
        standard_bid = int(standard_bid * multiplier)

#damn we're winning, js bid standard amt
    else:
        multiplier = 1 

#just in case, don't bid under 1 and don't bid more than we have...the game crashed so many times that i had to add this
    return max(1, min(standard_bid, my_bananas))
