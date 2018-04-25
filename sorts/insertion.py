from random import randint
def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            # if the current number is less than
            # the number before it, swap them
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

test_array = [randint(0,100000) for i in range(10)]
test_array_before = list(test_array)
insertionSort(test_array)
assert test_array == sorted(test_array_before)
