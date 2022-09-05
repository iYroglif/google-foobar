def solution(l):
    l.sort()

    sm = 0
    # idx12 index of min value that % 3 = 1, idx11 second min
    # idx22 index of min value that % 3 = 2, idx21 second min
    idx11 = idx12 = idx21 = idx22 = -1
    for i in range(len(l)):
        rem = l[i] % 3
        if rem == 0:
            continue
        elif rem == 1:
            if idx11 == -1:
                if idx12 == -1:
                    idx12 = i
                else:
                    idx11 = i
        elif idx21 == -1:
            if idx22 == -1:
                idx22 = i
            else:
                idx21 = i
        sm += l[i]

    rem = sm % 3
    if rem == 1:
        if idx12 != -1:
            l.pop(idx12)
        elif idx21 != -1:
            l.pop(idx22)
            l.pop(idx21)
        else:
            return 0
    elif rem == 2:
        if idx22 != -1:
            l.pop(idx22)
        elif idx11 != -1:
            l.pop(idx12)
            l.pop(idx11)
        else:
            return 0

    res = 0
    for d in reversed(l):
        res = res * 10 + d

    return res
