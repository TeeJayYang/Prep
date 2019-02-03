import math
def turans(n, k):
    return (k-1)*n*n/(2*k)

def turans2(n, k):
    return 0.5*(n**2 - (n % k)*math.ceil((n/k))**2 - (k - (n % k))*math.floor((n/k))**2)

def clique(n, m):
    if (m == 1):
        return 2
    high, low = n, 1
    if m > n*(n-1)/2:
        return n + 1
    elif m == n*( n-1 )/2:
        return n
    while (high >= low):
        max_clique = (high + low)//2

        max_edges = turans2(n, max_clique) 
        max_edges1 = turans2(n, max_clique + 1)
        if max_edges == m:
            return int(max_clique)
        elif max_edges < m and max_edges1 >= m:
            return int(max_clique + 1)
        elif max_edges1 < m:
            low = max_clique + 1
        else:
            high = max_clique - 1

def main():
    with open("input.txt") as f1:
        inp = [(int(line.split()[0]), int(line.split()[1])) for line in f1]
    with open("output.txt") as f2:
        out = [int(line) for line in f2]
    failed = 0
    # for i in range(100):
    for i in range(len(inp)):
        try: 
            n, m = inp[i][0], inp[i][1]
            ret = clique(n, m)
            o = out[i]
            assert(ret == o)
        except AssertionError as e:
            print("TestCase: {} ====> N: {}, M: {}, Expected output: {}, Got: {}".format(i, n,m,o,ret))
            failed += 1
    print("Test cases failed: {}".format(failed))

main()
