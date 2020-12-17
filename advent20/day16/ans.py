import re

# populates field_ranges, my_ticket
with open('input') as file:
    field_ranges = {}
    nearby_tickets = []

    field_pattern = re.compile(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')
    while True:
        line = file.readline()
        field_line = field_pattern.match(line.strip())
        if field_line:
            field_name = field_line.group(1)
            ranges = tuple(map(int, field_line.groups()[1:]))
            field_ranges[field_name] = ranges
        else:
            break

    file.readline()

    my_ticket = list(map(int, file.readline().strip().split(',')))

    file.readline()
    file.readline()

    for line in file:
        nearby_tickets.append(list(map(int, line.strip().split(','))))


def find_invalid_values(field_ranges, nearby_tickets):
    # pre process all valid values
    valid_values = [False] * (max(map(max, field_ranges.values())) + 1)
    for ranges in field_ranges.values():
        low1, hi1 = ranges[0], ranges[1]
        low2, hi2 = ranges[2], ranges[3]
        valid_values[low1:hi1 + 1] = [True] * (hi1 + 1 - low1)
        valid_values[low2:hi2 + 1] = [True] * (hi2 + 1 - low2)

    # find all invalid values
    valid_tickets = []
    invalid_values = []
    for ticket in nearby_tickets:
        valid = True
        for num in ticket:
            if num >= len(valid_values) or not valid_values[num]:
                invalid_values.append(num)
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return valid_tickets, invalid_values


def find_field_names(field_ranges, valid_tickets):
    possible_fields = []
    num_fields = len(field_ranges)
    for i in range(num_fields):
        possible_fields.append(set(field_ranges.keys()))

    for ticket in valid_tickets:
        for idx, num in enumerate(ticket):
            invalid_fields = set()
            for possible_field in possible_fields[idx]:
                ranges = field_ranges[possible_field]
                low1, hi1 = ranges[0], ranges[1]
                low2, hi2 = ranges[2], ranges[3]
                if not (low1 <= num <= hi1 or low2 <= num <= hi2):
                    invalid_fields.add(possible_field)
            possible_fields[idx] -= invalid_fields

    correct_fields = ['placeholder'] * num_fields
    fields_found = 0
    while fields_found < num_fields:
        for idx, possible_field in enumerate(possible_fields):
            if len(possible_field) == 1:
                correct_fields[idx] = list(possible_field)[0]
                fields_found += 1
                for pf in possible_fields:
                    pf.discard(correct_fields[idx])

    assert 'placeholder' not in correct_fields
    assert len(set(correct_fields)) == len(correct_fields)
    return correct_fields


valid_tickets, invalid_values = find_invalid_values(field_ranges,
                                                    nearby_tickets)
valid_tickets.append(my_ticket)

# part 1
print(sum(invalid_values))

# part 2
fields = find_field_names(field_ranges, valid_tickets)
ans = 1
for idx, field in enumerate(fields):
    if 'departure' in field:
        ans *= my_ticket[idx]
print(ans)
