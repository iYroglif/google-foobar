def solution(n):
    if n == '0':
        return 0
    res = 0  # number of operations
    ons = 0  # number of ones
    while n != '1':
        if int(n[-1]) % 2 == 0:
            if ons == 0:
                res += 1
            elif ons == 1:
                res += 3
                ons = 0
            else:
                res = res + ons + 1
                ons = 1
        else:
            ons += 1
        add = 0
        for i in range(len(n)):
            nmb = int(n[i])
            n = n[:i] + str(nmb // 2 + add) + n[i+1:]
            add = (nmb % 2) * 5
        if n[0] == '0':
            n = n[1:]
    if ons == 0:
        return res
    elif ons == 1:
        return res + 2
    return res + ons + 2
