def solution(s):
    re = 0  # count of employees walking to the right
    sal = 0  # count of salutes / 2
    for chr in s:
        if chr == '-':
            continue
        elif chr == '>':
            re += 1
        else:
            sal += re
    return sal * 2
