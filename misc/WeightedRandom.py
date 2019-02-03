from random import random
def RNG(weights):
    # weights is a dictionary of weights
    total = sum(weights.values())
    num = random() * total
    interval = 0
    for k,v in weights.items():
        if num <= interval + v and num > interval:
            return k
        interval += v

print(RNG({'a':40, 'b':20, 'c':50}))
