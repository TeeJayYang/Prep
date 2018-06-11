#given value and list of coins, how many ways can you make change
def coinChange(x, coins):
    dp = [0]*(n+1)
    dp = {}

    # if x = 0, there is 1 way to make change
    dp[0] = 1

    for c in coins:
        for value in range(c,n+1):
            dp[value] = dp.get(value,0) + dp[value-c] 
            print (dp)
    return dp[x]

arr = [1,2,3]
n = 4
print(coinChange(n, arr))
