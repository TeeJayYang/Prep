def BinAdd(str1, str2):
    maxlen = max(len(str1), len(str2))
    str1 = '0'*(maxlen - len(str1)) + str1
    str2 = '0'*(maxlen - len(str2)) + str2
    carry = 0
    ret = ''
    for i in range(1, maxlen+1):
        add = int(str1[-i]) + int(str2[-i]) + carry
        carry = 1 if add >= 2 else 0
        add %= 2
        ret = str(add) + ret
    ret = str(carry) + ret
    ret = ret.lstrip('0')
    if ret == '':
        ret = str(0)
    return ret

print(BinAdd('0000000000000000000', '0000'))
print(BinAdd('11111', '1'))
print(BinAdd('000000000000', '1'))
