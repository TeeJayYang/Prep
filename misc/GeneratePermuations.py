def permuation(strings, string, index=0):
    string = list(string)
    if index == len(string):
        strings.append(''.join(string))
        return
    for i in range(index, len(string)):
        temp = string[:]
        temp[index], temp[i] = temp[i], temp[index]
        permuation(strings, temp, index + 1)

out = []
permuation(out, 'asdf')
print(len(out))
