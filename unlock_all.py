import subprocess


def get_code(target):
    proc = subprocess.Popen('toy_lock.exe u', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ret = proc.communicate(input=('%s\n' % str(target)).encode())
    ret = ret[0].decode()[:-1]
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


def unlock_all(target):
    for i in range(len(target)):
        target_wc = add_check(target, i)
        code = get_code(target_wc)
        print(code)


if __name__ == '__main__':
    unlock_all("5756")
