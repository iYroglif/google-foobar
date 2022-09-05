def solution(x, y):
    x = int(x)
    y = int(y)
    i = 0  # generations
    while x != 1 and y != 1:
        if x < y:
            i += y // x
            y = y % x
            if y == 0:
                return 'impossible'
        elif y < x:
            i += x // y
            x = x % y
            if x == 0:
                return 'impossible'
        else:
            return 'impossible'
    return str(i + x + y - 2)
