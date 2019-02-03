from timeit import timeit

# Return all pairs of numbers that have a sum equal to a number k. Do not include pairs that are the same numbers in different order.
def test():
    def twosum(nums, k):
        ret = set()
        seen = set()
        for each in nums:
            comp = k - each
            if comp in seen:
                ret.add((each, comp))
            else:
                seen.add(each)
        return list(ret)

    # print(twosum([0,1,2,3,3,3,4,5,5,6], 6))

    l = [0,1,2,3,3,4,3,2,5,6,0,7]
    return twosum(l, 6)

def test2():
    def SumPairs(nums, k):
        seen = {}
        ret = []
        for i in nums:
            if seen.get(i, 0) >= 1 and i * 2 != k:
                continue
            else:
                complement = k - i
                count = seen.get(complement, 0)
                if (complement != i and count >= 1) or (complement == i and count == 1):
                    ret.append((complement, i))
            seen[i] = seen.get(i,0) + 1
        return ret

    l = [0,1,2,3,3,4,3,2,5,6,0,7]
    return SumPairs(l, 6)

print(test())
print(test2())
print(timeit(test))
print(timeit(test2))
