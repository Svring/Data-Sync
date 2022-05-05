while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            addition = take_turn(num_rolls, score1, dice)
            score0 += addition
            if is_swap(score0, score1):
                score0, score1 = score1, score0
        else:
            num_rolls = strategy1(score1, score0)
            addition = take_turn(num_rolls, score0, dice)
            score1 += addition
            if is_swap(score1, score0):
                score0, score1 = score1, score0
        who = other(who)