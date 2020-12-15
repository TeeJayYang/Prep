import re
from itertools import product

instructions = []

with open('input') as file:
    instructions = [line.strip() for line in file.readlines()]

bitmask_pattern = re.compile(r'mask = ((?:X|1|0){36})')
memset_pattern = re.compile(r'mem\[([0-9]+)\] = ((?:[0-9])+)')


def execute(instructions):
    mem = {}
    mask_or = 0  # sets required 1s
    mask_and = int('1' * 36, 2)  # sets required 0s
    for instruction in instructions:
        bitmask = bitmask_pattern.match(instruction)
        memset = memset_pattern.match(instruction)
        if bitmask:
            mask_or = 0  # sets required 1s
            mask_and = int('1' * 36, 2)  # sets required 0s
            for index, bit in enumerate(bitmask.group(1)[::-1]):
                if bit == '1':
                    mask_or |= 1 << index
                elif bit == '0':
                    mask_and &= ~(1 << index)
        elif memset:
            pos = int(memset.group(1))
            val = int(memset.group(2))
            val |= mask_or
            val &= mask_and
            mem[pos] = val
    return mem


def find_permutations(num, positions):
    all_nums = []
    prod = product((0, 1), repeat=len(positions))
    for permutation in prod:
        temp = num
        for x_idx, val in zip(positions, permutation):
            temp &= ~(1 << x_idx)  # clear bit
            temp |= val << x_idx  # set bit
        all_nums.append(temp)
    return all_nums


def execute2(instructions):
    mem = {}
    x_idx = []
    mask_or = 0  # sets required 1s
    for instruction in instructions:
        bitmask = bitmask_pattern.match(instruction)
        memset = memset_pattern.match(instruction)
        if bitmask:
            x_idx = []
            mask_or = 0  # sets required 1s
            for index, bit in enumerate(bitmask.group(1)[::-1]):
                if bit == '1':
                    mask_or |= 1 << index
                elif bit == 'X':
                    x_idx.append(index)
        elif memset:
            pos = int(memset.group(1))
            val = int(memset.group(2))
            pos |= mask_or
            perm = find_permutations(pos, x_idx)
            for p in perm:
                mem[p] = val
    return mem


# part 1
print(sum(execute(instructions).values()))

# part 2
print(sum(execute2(instructions).values()))
