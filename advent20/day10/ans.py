adapters = []
with open('input') as file:
    adapters.append(0)
    for line in file:
        adapters.append(int(line))
adapters.sort()
adapters.append(adapters[-1] + 3)


def find_diffs(adapters):
    diffs = []
    prev = 0
    for adapter in adapters[1:]:
        diff = adapter - prev
        assert 1 <= diff <= 3
        prev = adapter
        diffs.append(diff)
    return diffs


def count_arrangements(adapters):
    dp = []
    for index, adapter in enumerate(adapters):
        if index == 0:
            dp.append(1)
            continue
        lookback = index - 1
        total = 0
        while lookback >= 0 and adapter - adapters[lookback] <= 3:
            total += dp[lookback]
            lookback -= 1
        dp.append(total)

    return dp[-1]


# part 1

diffs = find_diffs(adapters)

jolt1 = diffs.count(1)
jolt3 = diffs.count(3)

print(jolt1 * jolt3)

print(count_arrangements(adapters))
