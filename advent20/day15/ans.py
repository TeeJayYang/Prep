puzzle_input = [15, 5, 1, 4, 7, 0]
initial_turns = dict((val, turn + 1) for turn, val in enumerate(puzzle_input))


def play(turns, target_turn):
    curr_turn = len(turns) + 1
    prev_num = 0
    while curr_turn < target_turn:
        if prev_num in turns:
            spoken = curr_turn - turns[prev_num]
            turns[prev_num] = curr_turn
            prev_num = spoken
        else:
            turns[prev_num] = curr_turn
            prev_num = 0
        curr_turn += 1
    return prev_num


# part 1
print(play(dict(initial_turns), 2020))

# part 2
print(play(dict(initial_turns), 3e7))
