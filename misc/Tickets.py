def findDest(tickets, dest=None):
    d = {}
    for t in tickets:
        d[t[0]] = t[1]
    if dest is None:
        dest = tickets[0][0]
    while dest in d:
        dest = d[dest]
    return dest

def findOrigin(tickets, origin=None):
    o = {}
    for t in tickets:
        o[t[1]] = t[0]
    if origin is None:
        origin = tickets[0][0]
    while origin in o:
        origin = o[origin]
    dest = findDest(tickets, origin)
    return (origin, dest)

def findMissing(origin, dest, tickets):
    to = findOrigin(tickets, dest)[0]
    fr = findDest(tickets, origin)
    return (fr, to)


ORIGINAL_TICKETS = [
    ('SFO', 'LAX'),
    ('LAX', 'JFK'),
    ('JFK', 'LHR'),
    ('LHR', 'CDG'),
    ('CDG', 'DXB'),
    ('DXB', 'HKG'),
    ('HKG', 'HAM'),
]

print(findDest(ORIGINAL_TICKETS, 'SFO'))
print(findOrigin(ORIGINAL_TICKETS))

ORIGINAL_TICKETS = [
    ('SFO', 'LAX'),
    ('LAX', 'JFK'),
    ('JFK', 'LHR'),
    ('LHR', 'CDG'),
    ('CDG', 'DXB'),
    # ('DXB', 'HKG'),
    ('HKG', 'HAM'),
]

print(findMissing('SFO', 'HAM', ORIGINAL_TICKETS))
