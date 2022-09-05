def solution(dimensions, your_position, trainer_position, distance):
    if your_position == trainer_position:
        return 0
    distance *= distance
    x = trainer_position[0] - your_position[0]
    y = trainer_position[1] - your_position[1]
    cur_dist = x**2 + y**2
    your_hits = set()  # beams which hit you
    if cur_dist == distance:
        return 1
    elif cur_dist > distance:
        return 0
    your_hits.add(((abs(x)*x)/float(cur_dist), (abs(y)*y)/float(cur_dist)))
    res = 1  # number of distinct directions
    lvl = 1  # reflections depth
    cur_your_pos = [0, 0]  # reflect your position
    cur_trainer_pos = [0, 0]  # reflect trainer position
    flg = True  # flag that at least one reflect at this depth <=distance
    while flg:
        flg = False
        for dim in [(0, 1), (1, 0)]:  # Left-Right Top-Bot
            for dir in [1, -1]:  # Top-Right Bot-Left
                # Right -> Left -> Top -> Bot
                if lvl % 2 == 0:
                    cur_your_pos[dim[0]] = your_position[dim[0]] + lvl * dimensions[dim[0]] * dir
                    cur_trainer_pos[dim[0]] = trainer_position[dim[0]] + lvl * dimensions[dim[0]] * dir
                else:
                    cur_your_pos[dim[0]] = dimensions[dim[0]] * lvl * dir + dimensions[dim[0]] - your_position[dim[0]]
                    cur_trainer_pos[dim[0]] = dimensions[dim[0]] * lvl * dir + dimensions[dim[0]] - trainer_position[dim[0]]
                for i in range(-lvl+1, lvl, 1):
                    if i % 2 == 0:
                        cur_your_pos[dim[1]] = your_position[dim[1]] + i * dimensions[dim[1]]
                        cur_trainer_pos[dim[1]] = trainer_position[dim[1]] + i * dimensions[dim[1]]
                    else:
                        cur_your_pos[dim[1]] = dimensions[dim[1]] * i + dimensions[dim[1]] - your_position[dim[1]]
                        cur_trainer_pos[dim[1]] = dimensions[dim[1]] * i + dimensions[dim[1]] - trainer_position[dim[1]]

                    x = cur_your_pos[0] - your_position[0]
                    y = cur_your_pos[1] - your_position[1]
                    cur_dist_your_pos = x**2 + y**2
                    dir_your_pos = ((abs(x)*x)/float(cur_dist_your_pos), (abs(y)*y)/float(cur_dist_your_pos))

                    x = cur_trainer_pos[0] - your_position[0]
                    y = cur_trainer_pos[1] - your_position[1]
                    cur_dist = x**2 + y**2

                    if cur_dist_your_pos < cur_dist:
                        if cur_dist_your_pos <= distance:
                            your_hits.add(dir_your_pos)
                        if cur_dist <= distance:
                            flg = True
                            direction = ((abs(x)*x)/float(cur_dist), (abs(y)*y)/float(cur_dist))
                            if direction not in your_hits:
                                your_hits.add(direction)
                                res += 1
                    else:
                        if cur_dist <= distance:
                            flg = True
                            direction = ((abs(x)*x)/float(cur_dist), (abs(y)*y)/float(cur_dist))
                            if direction not in your_hits:
                                your_hits.add(direction)
                                res += 1
                        if cur_dist_your_pos <= distance:
                            your_hits.add(dir_your_pos)

        if flg:  # edges
            for dir in [1, -1]:  # Right Left
                if lvl % 2 == 0:
                    cur_your_pos[0] = your_position[0] + lvl * dimensions[0] * dir
                    cur_trainer_pos[0] = trainer_position[0] + lvl * dimensions[0] * dir
                else:
                    cur_your_pos[0] = dimensions[0] * lvl * dir + dimensions[0] - your_position[0]
                    cur_trainer_pos[0] = dimensions[0] * lvl * dir + dimensions[0] - trainer_position[0]
                for i in [lvl, -lvl]:  # Top Bot
                    # Right-Top -> Right-Bot -> Left-Top -> Left-Bot
                    if lvl % 2 == 0:
                        cur_your_pos[1] = your_position[1] + i * dimensions[1]
                        cur_trainer_pos[1] = trainer_position[1] + i * dimensions[1]
                    else:
                        cur_your_pos[1] = dimensions[1] * i + dimensions[1] - your_position[1]
                        cur_trainer_pos[1] = dimensions[1] * i + dimensions[1] - trainer_position[1]

                    x = cur_your_pos[0] - your_position[0]
                    y = cur_your_pos[1] - your_position[1]
                    cur_dist_your_pos = x**2 + y**2
                    dir_your_pos = ((abs(x)*x)/float(cur_dist_your_pos), (abs(y)*y)/float(cur_dist_your_pos))

                    x = cur_trainer_pos[0] - your_position[0]
                    y = cur_trainer_pos[1] - your_position[1]
                    cur_dist = x**2 + y**2

                    if cur_dist_your_pos < cur_dist:
                        if cur_dist_your_pos <= distance:
                            your_hits.add(dir_your_pos)
                        if cur_dist <= distance:
                            direction = ((abs(x)*x)/float(cur_dist), (abs(y)*y)/float(cur_dist))
                            if direction not in your_hits:
                                your_hits.add(direction)
                                res += 1
                    else:
                        if cur_dist <= distance:
                            direction = ((abs(x)*x)/float(cur_dist), (abs(y)*y)/float(cur_dist))
                            if direction not in your_hits:
                                your_hits.add(direction)
                                res += 1
                        if cur_dist_your_pos <= distance:
                            your_hits.add(dir_your_pos)

        lvl += 1

    return res
