def permute(string):
    ret = []
    def permute_helper(string, index=0):
        if index == len(string):
            ret.append(''.join(string))
        for i in range(index, len(string)):
            temp = list(string)
            temp[i], temp[index] = temp[index], temp[i]

            permute_helper(temp, index+1)
    permute_helper(string)
    return ret

print(permute('asdf'))
print(permute(''))
