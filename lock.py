def lock4_no_check(target, check):
    a, b, c, d = map(int, target)
    w = x = y = z = ""
    if check == 0:
        w = a + 0
        y = b + 7
        z = c + 0
        x = d + 4
    elif check == 1:
        w = b - 9
        x = a - 5
        y = c - 7
        z = d - 6
    elif check == 2:
        w = a - 7
        x = b - 3
        y = c - 4
        z = d - 5
    elif check == 3:
        w = a + 3
        y = b + 0
        z = c + 7
        x = d + 1
    ret = [w, x, y, z]
    ret = map(lambda ex: str(ex % 10), ret)
    return "".join(ret)


def lock_hyper4_no_check(target, check, hyper):
    lock4_no_check(target+hyper, check)


def lock_u4_no_check(target, check):
    if len(target) == 1:
        return target
    if len(target) == 2:
        a, b = map(int, target)
        z = y = ""
        if check == 0:
            y = a + 0
            z = b + 1
        elif check == 1:
            z = a + 5
            y = b + 1
        ret = [y, z]
        ret = map(lambda ex: str(ex % 10), ret)
        return "".join(ret)
    if len(target) == 3:
        a, b, c = map(int, target)
        x = y = z = ""
        if check == 0:
            x = a + 0
            z = b + 5
            y = c + 3
        elif check == 1:
            y = a + 5
            x = b + 1
            z = c + 3
        elif check == 2:
            y = a + 8
            z = b + 7
            x = c + 1
        ret = [x, y, z]
        ret = map(lambda ex: str(ex % 10), ret)
        return "".join(ret)


def add_check(target, check):
    bit_sum = 0
    for i in range(len(target)):
        bit_sum += int(target[i])
    bit_sum %= 10
    cv = (10 - bit_sum + check) % 10
    check = len(target) - check
    target = target[:check] + str(cv) + target[check:]
    return target


def lock_ue4_check(target, check):
    if len(target) == 4:
        target = lock4_no_check(target, check)
    else:
        target = lock_u4_no_check(target, check)
    target = add_check(target, check)
    return target


if __name__ == '__main__':
    print(lock4_no_check("9999", 0))
