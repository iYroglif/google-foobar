from math import factorial
from fractions import gcd
from collections import Counter


def solution(w, h, s):
    def count(c, n):
        cnt = factorial(n)
        for a, b in Counter(c).items():
            cnt //= (a**b)*factorial(b)
        return cnt

    def partitions(n, i=1):
        yield [n]
        for i in range(i, n//2 + 1):
            for p in partitions(n-i, i):
                yield [i] + p

    res = 0
    for pw in partitions(w):
        for ph in partitions(h):
            m = count(pw, w)*count(ph, h)
            res += m*(s**sum([sum([gcd(i, j) for i in pw]) for j in ph]))

    return str(res//(factorial(w)*factorial(h)))
