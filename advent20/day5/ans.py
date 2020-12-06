seats = []
with open('input') as file:
    for line in file:
        seats.append(line.strip())


def parse_id(seat):
    row_low, row_high = 0, 127
    col_low, col_high = 0, 7
    for c in seat:
        if c == 'B':
            row_low = (row_low + row_high) // 2 + 1
        elif c == 'F':
            row_high = (row_low + row_high) // 2
        elif c == 'R':
            col_low = (col_low + col_high) // 2 + 1
        elif c == 'L':
            col_high = (col_low + col_high) // 2
    assert (row_low == row_high)
    assert (col_low == col_high)

    return row_low * 8 + col_low


def find_max_id(seats):
    max_id = 0
    for seat in seats:
        max_id = max(max_id, parse_id(seat))
    return max_id


def find_missing_seat(seats):
    id_sum = 0
    max_id = 0
    min_id = float('inf')
    for seat in seats:
        seat_id = parse_id(seat)
        max_id = max(max_id, seat_id)
        min_id = min(min_id, seat_id)
        id_sum += seat_id

    # difference between sum of all available seats
    # and all filled seats is your seat
    return int((max_id + min_id) * (max_id - min_id + 1) / 2 - id_sum)


# part 1
print(find_max_id(seats))

# part 2
print(find_missing_seat(seats))
