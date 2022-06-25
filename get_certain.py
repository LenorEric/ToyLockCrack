import subprocess


def get_diff(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return i


def get_code(target):
    proc = subprocess.Popen('toy_lock.exe l', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ret = proc.communicate(input=('%s\n' % str(target)).encode())
    ret = ret[0].decode()[:-1]
    return ret


def de_calc_check_pos(code):
    bit_sum = 0
    while code:
        bit_sum += code % 10
        code //= 10
    bit_sum %= 10
    return bit_sum


def remove_check(code):
    cp = de_calc_check_pos(int(code))
    cs = str(code)
    cp = len(cs) - cp
    cs = cs[:cp - 1] + cs[cp:]
    return cs


def get_certain_c(target, c):
    code = get_code(target)
    while de_calc_check_pos(int(code)) != c:
        code = get_code(target)
    code = remove_check(code)
    return code


def certain_shift(target, shift):
    for i in range(len(str(target))):
        print(len(str(target)) - i - 1, end="")
    print()
    for xxx in range(target, target + 10 ** (shift + 1), 10 ** shift):
        print(get_certain_c(xxx, 0))


def try_shift(suffix):
    sums = int(suffix) + len(suffix)
    return sums


def bit_minus(a_, b_):
    ret = ""
    for i in range(len(a_)):
        ret += str((int(a_[i]) - int(b_[i])) % 10)
    return ret


if __name__ == '__main__':
    a = get_certain_c("000000000000000000000000000000000000000000000", 1)
    print(a)
