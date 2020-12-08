from operator import and_, or_
from functools import reduce

groups = []

with open('input') as file:
    group = []
    for line in file:
        if line == '\n':
            groups.append(group)
            group = []
            continue
        bitflag = 0
        for c in line.strip():
            bitflag |= 1 << (ord(c) - ord('a'))
        group.append(bitflag)
    groups.append(group)


def count_bits(x, reducer):
    return bin(reduce(reducer, x)).count('1')


# part 1
print(sum([count_bits(group, or_) for group in groups]))

# part 2
print(sum([count_bits(group, and_) for group in groups]))
