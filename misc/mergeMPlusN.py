def moveToEnd(n2):
    i = len(n2) - 1
    for j in range(len(n2)-1, -1, -1):
        if n2[j] is not None:
            n2[i], n2[j] = n2[j], None
            i -= 1
    return i + 1

def merge(nlarge, nsmall):
    li = moveToEnd(nlarge)
    i = 0 # merge index
    j = 0 # nsmall index
    while li < len(nlarge) and j < len(nsmall):
        if nlarge[li] <= nsmall[j]:
            nlarge[i] = nlarge[li]
            li += 1
            i += 1
        else:
            nlarge[i] = nsmall[j]
            j += 1
            i += 1

    while li < len(nlarge):
        nlarge[i] = nlarge[li]
        li += 1
        i += 1

    while j < len(nsmall):
        nlarge[i] = nsmall[j]
        j += 1
        i += 1

def main():
    n1 = [ 2, None, 5, None, 7 , 8, None]
    n2 = [1, 4, 5]
    merge(n1, n2)
    print(n1)

main()
