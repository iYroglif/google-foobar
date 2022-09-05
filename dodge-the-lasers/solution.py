def solution(s):
    s = int(s)
    fractions = [(1, 1), (3, 2)]  # continued fractions of sqrt(2)
    while fractions[-1][1] <= s:
        fractions.append(
            (fractions[-1][0]*2 + fractions[-2][0], fractions[-1][1]*2 + fractions[-2][1]))
    i = len(fractions) - 2
    res = 0
    while s > 1:
        while fractions[i][1] >= s:
            i -= 1
        b = s // fractions[i][1]
        s = s % fractions[i][1]
        tmp1 = b * fractions[i][0]
        if i % 2 == 0:
            tmp2 = tmp1*fractions[i][1] - fractions[i][1] + fractions[i][0] + 1
        else:
            tmp2 = tmp1*fractions[i][1] - fractions[i][1] + fractions[i][0] - 1
        res += ((b*tmp2)//2) + s*tmp1
    if s == 1:
        res += 1
    return str(res)
