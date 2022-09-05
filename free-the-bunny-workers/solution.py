from itertools import combinations


def solution(num_buns, num_required):
    res = [[] for _ in range(num_buns)]
    combs = combinations(range(num_buns), num_buns - num_required + 1)
    i = 0
    for comb in combs:
        for k in comb:
            res[k].append(i)
        i += 1
    return res
