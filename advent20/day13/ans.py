from collections import namedtuple
from math import ceil

with open('input') as file:
    earliest = int(file.readline())
    bus_ids = file.readline().split(',')


def find_earliest_bus(earliest, bus_ids):
    next_bus_time = float('inf')
    next_bus_id = 0
    for bus_id in bus_ids:
        if bus_id == 'x':
            continue
        bus_id = int(bus_id)
        arrival = ceil(earliest / bus_id) * bus_id
        if arrival < next_bus_time:
            next_bus_time = arrival
            next_bus_id = bus_id
    return next_bus_time, next_bus_id


BusOffset = namedtuple('BusOffset', 'id, offset')


def find_subsequent_bus_time(bus_ids):
    buses = []
    for index, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            buses.append(BusOffset(int(bus_id), index))
    base = buses[0]
    mult = 1
    increment = 1
    next_time = 0
    for bus in buses[1:]:
        while True:
            next_time = base.id * mult + bus.offset
            if next_time % bus.id == 0:
                increment = bus.id if increment == 1 else increment * bus.id
                break
            else:
                mult += increment
    return base.id * mult


# part 1
bus_time, bus_id = find_earliest_bus(earliest, bus_ids)
print((bus_time - earliest) * bus_id)

# part 2
print(find_subsequent_bus_time(bus_ids))
