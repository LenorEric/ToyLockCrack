def encrypt(a, b, c, const):
    a = int(a)
    b = int(b)
    c = int(c)
    return str((a + b + c + const) % 10)


def lock_with_swap(target, check):
    ret = ""
    pro_len = check % 3 + 1
    remain = len(target)
    curr = 0
    while remain:
        if pro_len == 1:
            ret += encrypt(curr, target[curr], check, 0)
        elif pro_len == 2:
            ret += encrypt(target[curr + 1], curr, - check, 2)
            ret += encrypt(target[curr], curr, check, 4)
        else:
            ret += encrypt(target[curr + 2], curr, - check, 3)
            ret += encrypt(target[curr], curr, check, 6)
            ret += encrypt(target[curr + 1], curr, - check, 9)
        curr += pro_len
        remain -= pro_len
        pro_len -= 1
        if pro_len == 0:
            pro_len = 3
        if pro_len > remain:
            pro_len = remain
    return ret


def add_check(target, check):
    bit_sum = 0
    for i in range(len(target)):
        bit_sum += int(target[i])
    bit_sum %= 10
    cv = (10 - bit_sum + check) % 10
    check = len(target) - check
    target = target[:check] + str(cv) + target[check:]
    return target


def gen_all_cip(target):
    ret = []
    for i in range(len(target)):
        ret.append(add_check(lock_with_swap(target, i), i))
    return ret


if __name__ == '__main__':
    print(gen_all_cip("123456789"))
