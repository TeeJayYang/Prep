from random import randint
"""
- Choose a pivot
- Partition the list such that
  the left partition has all the elements
  less than the pivot and the right
  partition has all the elements greater
  than the pivot
- Put the pivot into the correct spot
  (count number of smaller elements than pivot)
"""
def _partition(nums, high, low):
    pivot = nums[high]
    pivotIndex = low

    # Move everything to the right partition
    for i in range(low,high):
        if nums[i] <= pivot:
            nums[pivotIndex], nums[i] = nums[i], nums[pivotIndex]
            pivotIndex += 1

    # Move the pivot to the right spot
    nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]
    return pivotIndex

def _qs(nums, high, low):
    if (high <= low):
        return

    pivotIndex = _partition(nums, high, low)

    _qs(nums, pivotIndex - 1, low)
    _qs(nums, high, pivotIndex + 1)

def QuickSort(nums):
    _qs(nums, len(nums) - 1, 0)

def main():
    arr = [randint(0,100) for _ in range(100)]
    unsorted = arr[:]
    QuickSort(arr)
    assert(arr == sorted(unsorted))

main()
