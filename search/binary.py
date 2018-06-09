# recursive
def binarySearchRecursive(nums, high, low, target):
    if high < low:
        return -1
    mid = low + (high-low)//2
    if nums[mid] == target:
        return mid
    if target > nums[mid]:
        return binarySearchRecursive(nums, high, mid+1, target)
    elif target < nums[mid]:
        return binarySearchRecursive(nums, mid-1, low, target)

# iterative
def binarySearchIterative(nums, high, low, target):
    while high >= low:
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
    return -1

# finds the first occurrence
def binarySearchFloor(nums, high, low, target):
    while high >= low:
        mid = low + (high-low)//2
        if nums[mid] == target and (mid == 0 or nums[mid] == target):
            return mid
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# finds the last occurrence
def binarySearchCeil(nums, high, low, target):
    while high >= low:
        mid = low + (high-low)//2
        if nums[mid] == target and (mid == len(nums) -1 or nums[mid+1] > target):
            return mid
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    nums = [1, 15, 25, 39, 62, 68, 70, 71, 72, 73, 79, 98, 109, 135, 136, 139, 141, 161, 164, 174, 182, 200, 210, 218, 226, 234, 236, 264, 272, 278, 282, 283, 324, 328, 348, 349, 374, 378, 379, 395, 396, 402, 426, 435, 442, 460, 463, 471, 474, 480, 482, 492, 495, 499, 508, 517, 543, 546, 553, 555, 576, 632, 638, 643, 646, 660, 694, 719, 723, 732, 747, 763, 765, 782, 800, 844, 849, 850, 858, 882, 890, 891, 893, 905, 918, 920, 926, 931, 935, 939, 942, 976, 979, 990, 999]
    targets = [290, 426, 990, 25, 632]
    for target in targets: 
        print('Binary Search Recursive: {}'.format (binarySearchRecursive(nums, len(nums)-1, 0, target)))
        print('Binary Search Recursive: {}'.format (binarySearchIterative(nums, len(nums)-1, 0, target)))
        try:
            print('Python find: {}'.format(nums.index(target)))
        except ValueError:
            print('Python find: {}'.format(-1))
    nums = [1, 1, 3, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 9, 9, 10, 10, 11, 11, 12, 12, 12, 12, 14, 15, 16, 16, 16, 16, 17, 18, 18, 18, 19, 19, 19, 21, 21, 22, 23, 24, 25, 25, 25, 25, 26, 26, 27, 27, 27, 28, 29, 30, 30, 30, 30, 30, 30, 31, 31, 33, 33, 33, 34, 34, 36, 37, 39, 40, 41, 41, 42, 42, 42, 42, 42, 43, 43, 44, 44, 46, 46, 47, 47, 48, 50, 50, 50, 50, 50, 51, 51, 53, 53, 54, 56, 56, 57, 57, 58]
    # floor testing
    targets = [0, 1, 58, 50, 5, 14, 15 , 52, 59]
    for target in targets:
        print('BinarySearchFloor: {}'.format(binarySearchFloor(nums, len(nums)-1, 0, target)))
        try:
            print('Python find: {}'.format(nums.index(target)))
        except ValueError:
            print('Python find: {}'.format(-1))
    # ceil testing
    for target in targets:
        print('BinarySearchCeil: {}'.format(binarySearchCeil(nums, len(nums)-1, 0, target)))
        try:
            print('Python find: {}'.format(len(nums)-1-nums[::-1].index(target)))
        except ValueError:
            print('Python find: {}'.format(-1))

main()
