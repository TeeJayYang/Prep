from collections import defaultdict, deque

nums = []

with open('input') as file:
    for line in file:
        nums.append(int(line))


def first_invalid(nums, preamble_len):
    sums = []

    for index, num in enumerate(nums):
        sums.append(set())
        valid = False or index < preamble_len
        for i in range(1, min(preamble_len, index) + 1):
            if num in sums[index - i]:
                valid = True
            sums[index - i].add(nums[index - i] + num)
        if not valid:
            return num


def find_contig_numbers(nums, target):
    contig = deque()
    total = 0
    for i in nums:
        contig.append(i)
        total += i
        while total > target:
            total -= contig.popleft()
        if total == target:
            return contig


# part 1
invalid_num = first_invalid(nums, 25)
print(invalid_num)

# part 2
contig = find_contig_numbers(nums, invalid_num)
print(max(contig) + min(contig))
