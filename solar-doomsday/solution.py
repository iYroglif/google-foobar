def solution(area):
    res = []
    while area > 0:
        up_bound = 1 << (area.bit_length() // 2) + 1
        x = area // up_bound
        while x < up_bound:
            up_bound = (up_bound + x) // 2
            x = area // up_bound
        res.append(up_bound*up_bound)
        area -= res[-1]
    return res
