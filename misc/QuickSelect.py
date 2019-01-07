from random import randint

## high low is inclusive indicies
def partition(nums, high, low):
    pivotIndex = randint(low, high)
    pivot = nums[pivotIndex]
    nums[high], nums[pivotIndex] = nums[pivotIndex], nums[high]
    smallI = low
    for i in range(low, high):
        if nums[i] <= pivot:
            nums[smallI], nums[i] = nums[i], nums[smallI]
            smallI += 1
    nums[smallI], nums[high] = nums[high], nums[smallI]
    return smallI
"""
Returns the kth smallest number in an unsorted array
with average time complexity of O(n)

k = 0 is the smallest element
"""
def QuickSelect(nums, k):
    low = 0
    high = len(nums) - 1
    while low < high:
        pivI = partition(nums, high, low)
        if pivI < k:
            low = pivI + 1
        elif pivI > k:
            high = pivI - 1
        else:
            break
    return nums[k]

A = [randint(0,100) for i in range(50)]
B = A[:]
assert(QuickSelect(A,0) == sorted(B)[0])
