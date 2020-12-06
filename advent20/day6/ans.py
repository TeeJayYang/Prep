from collections import defaultdict

groups = []

with open('input') as file:
    group_size = 0
    group = defaultdict(int)
    for line in file:
        if line == '\n':
            groups.append((group, group_size))
            group_size = 0
            group = defaultdict(int)
            continue
        for c in line.strip():
            group[c] += 1
        group_size += 1
    groups.append((group, group_size))

# any% speedrun one liners

# part 1
print(sum(map(lambda x: len(x[0]), groups)))

# part 2
print(sum(map(lambda x: len([k for k, v in x[0].items() if v == x[1]]), groups)))
