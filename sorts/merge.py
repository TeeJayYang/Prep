def merge1(nums, left, mid, right):
    leftSize = mid - left + 1
    rightSize = right - mid

    L = [0] * leftSize
    R = [0] * rightSize

    # copy
    for i in range(leftSize):
        L[i] = nums[left+i]

    for i in range(rightSize):
        R[i] = nums[mid+1+i]

    #merge
    l = 0
    r = 0
    i = left
    while l < len(L) and r < len(R):
        if L[l] <= R[r]:
            nums[i] = L[l]
            l +=1
        else:
            nums[i] = R[r]
            r +=1
        i += 1

    #copying over remainder
    while l < len(L):
        nums[i] = L[l]
        l += 1
        i += 1

    while r < len(R):
        nums[i] = R[r]
        r += 1
        i += 1

def mergeSort1(nums, left, right):
    if left >= right:
        return

    mid = (right + left)//2

    #sort each half
    mergeSort1(nums, left, mid)
    mergeSort1(nums, mid+1, right)
    merge1(nums, left, mid, right)

def merge2(left,right):
    ret = [0]*(len(left)+ len(right))

    l = 0
    r = 0
    i = 0 
    while l< len(left) and r < len(right):
        if left[l] <= right[r]:
            ret[i] = left[l]
            l += 1
        else:
            ret[i] = right[r]
            r += 1
        i += 1

    while l < len(left):
        ret[i] = left[l]
        l += 1
        i += 1

    while r < len(right):
        ret[i] = right[r]
        r += 1
        i += 1
    
    return ret

def mergeSort2(nums, left, right):
    if left >= right:
        return

    mid = (right + left)//2

    #sort each half
    mergeSort2(nums, left, mid)
    mergeSort2(nums, mid+1, right)
    nums[left:right] = merge2(nums[left:mid], nums[mid:right])

def mergeSortIterative(nums):
    for j in range(1, len(nums)):
        j *= 2
        print(nums)
        for i in range(0,len(nums), j):
            n1 = nums[i:i+(j/2)]
            n2 = nums[i+(j/2):i+j]
            print( "  {}".format(n1) )
            print( "  {}".format(n2) )
            l = r = 0
            merged = []
            while l < len(n1) and r < len(n2):
                if n1[l] <= n2[r]:
                    merged.append(n1[l])
                    l += 1
                else:
                    merged.append(n2[r])
                    r += 1
            while l < len(n1):
                merged.append(n1[l]) 
                l += 1
            while r < len(n2):
                merged.append(n2[r]) 
                r += 1
            print(' {}'.format(merged))
            nums[i:i+j] = merged
def main():
    nums = [12, 11, 13, 5, 6, 7]
    print (nums)
    print('Python sort: {}'.format(sorted(nums)))
    mergeSort1(nums, 0 , len(nums)-1)
    print('MergeSort: {}'.format(nums))
    nums = [12, 11, 13, 5, 6, 7]
    mergeSort2(nums, 0 , len(nums)-1)
    print('MergeSort: {}'.format(nums))
    nums = [12, 11, 13, 5, 6, 7]
    mergeSortIterative(nums)
    print('MergeSortIter: {}'.format(nums))

main()
