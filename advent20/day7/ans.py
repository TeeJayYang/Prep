import re
from collections import defaultdict

lookup = {}
rev_lookup = defaultdict(dict)
with open('input') as file:
    for line in file:
        match = re.search(r'(.+) bags contain (.+)\.', line)
        if not match:
            raise Exception(f'No match: {line}')
        parent = match.group(1)
        children = match.group(2).split(',')

        children_dict = {}
        for child in children:
            match = re.search(r'(\d+) (.+) bags?', child)
            if not match:
                continue
            children_dict[match.group(2).strip()] = int(match.group(1))

        for child, amount in children_dict.items():
            rev_lookup[child][parent] = amount
        lookup[parent] = children_dict


# def find_holders(bag, lookup, holders=set()):
#     if bag in holders:
#         return
#     immediate_holders = lookup[bag]
#     for bag in immediate_holders:
#         find_holders(bag, lookup)
#     holders.update(immediate_holders)
#     return holders


def find_holders2(bag, lookup, holders={}):
    if bag in holders:
        return (holders, holders[bag])
    immediate_holders = lookup[bag]
    total = 0
    for bag, num_bags in immediate_holders.items():
        bag_val = find_holders2(bag, lookup)[1]
        holders[bag] = bag_val
        total += bag_val * num_bags
    return (holders, total + sum(immediate_holders.values()))


# part 1
print(len(find_holders2('shiny gold', rev_lookup)[0]))

# part 2
print(find_holders2('shiny gold', lookup)[1])
