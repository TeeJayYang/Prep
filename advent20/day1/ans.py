def twosum(nums, target):
    comp = set()
    for i in nums:
        if target - i in comp:
            return (i, target - i, i * (target - i))
            break
        comp.add(i)


def threesum(nums, target):
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while k > j:
            res = nums[i] + nums[j] + nums[k]
            if res > target:
                k -= 1
            elif res < target:
                j += 1
            else:
                return (nums[i], nums[j], nums[k], nums[i] * nums[j] * nums[k])


nums = []
target = 2020
with open('input') as file:
    for line in file:
        nums.append(int(line))
    print(len(nums))
    print(*twosum(nums, target))
    print(*threesum(nums, target))
