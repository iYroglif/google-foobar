def solution(n):
    calculated = [1, *[0]*n]
    tmp = 0
    for i in range(1, n):
        tmp += i-1
        if tmp > n-i:
            tmp = n-i
        for j in range(tmp, -1, -1):
            calculated[j+i] += calculated[j]
    return calculated[n]
