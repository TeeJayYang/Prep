from collections import namedtuple

seats = []
with open('input') as file:
    for line in file:
        seats.append(list(line.strip()))


Index = namedtuple('index', 'x, y')
Directions = namedtuple('directions', 'N, NE, E, SE, S, SW, W, NW')

directions = Directions(N=Index(0, -1),
                        NE=Index(1, -1),
                        E=Index(1, 0),
                        SE=Index(1, 1),
                        S=Index(0, 1),
                        SW=Index(-1, 1),
                        W=Index(-1, 0),
                        NW=Index(-1, -1))


def check_direction(seats, idx, direction, part1):
    new_idx = Index(idx.x, idx.y)
    new_seat = None
    while True:
        new_idx = Index(new_idx.x + direction.x, new_idx.y + direction.y)
        if new_idx.x < 0 or new_idx.y < 0 or not new_idx.y < len(
                seats) or not new_idx.x < len(seats[0]):
            break
        new_seat = seats[new_idx.y][new_idx.x]
        if part1 or new_seat == '#' or new_seat == 'L':
            break
    return new_seat


def change_state(seats, part1):
    changed = False
    new_seats = []
    for row_index, row in enumerate(seats):
        new_row = []
        for seat_index, seat in enumerate(row):
            if seat == 'L':
                no_occupied = True
                for direction in directions:
                    new_seat = check_direction(seats,
                                               Index(seat_index, row_index),
                                               direction, part1)
                    if new_seat == '#':
                        no_occupied = False
                        break
                if no_occupied:
                    new_row.append('#')
                    changed = True
                else:
                    new_row.append('L')
            elif seat == '#':
                occupied_count = 0
                for direction in directions:
                    new_seat = check_direction(seats,
                                               Index(seat_index, row_index),
                                               direction, part1)
                    if new_seat == '.':
                        continue
                    elif new_seat == '#':
                        occupied_count += 1
                if occupied_count > 4 or part1 and occupied_count == 5:
                    new_row.append('L')
                    changed = True
                else:
                    new_row.append('#')
            elif seat == '.':
                new_row.append('.')
        new_seats.append(new_row)
    return new_seats, changed


def print_state(seats):
    print('=======================================')
    for row in seats:
        print(''.join(row))


def find_final_state(seats, part1=True):
    changed = True
    new_seats = seats
    while changed:
        # print_state(new_seats)
        new_seats, changed = change_state(new_seats, part1)
    return new_seats


# part 1
print(sum(row.count('#') for row in find_final_state(seats)))

# part 2
print(sum(row.count('#') for row in find_final_state(seats, part1=False)))
