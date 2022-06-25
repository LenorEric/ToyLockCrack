import subprocess


def get_code(target):
    proc = subprocess.Popen('toy_lock.exe l', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ret = proc.communicate(input=('%s\n' % str(target)).encode())
    ret = ret[0].decode()[:-1]
    return int(ret)


def de_calc_check_pos(code):
    bit_sum = 0
    while code:
        bit_sum += code % 10
        code //= 10
    bit_sum %= 10
    return bit_sum


def remove_check(code):
    cp = de_calc_check_pos(code)
    cs = str(code)
    cp = len(cs) - cp
    cs = cs[:cp - 1] + cs[cp:]
    return int(cs)


def get_certain_c(target, c):
    code = get_code(target)
    while de_calc_check_pos(code) != c:
        code = get_code(target)
    return code


def print_ret():
    return get_certain_c(11000000, 0)


if __name__ == '__main__':
    print(print_ret())
