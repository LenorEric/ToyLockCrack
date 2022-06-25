from get_certain import get_certain_c


def get_diff(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return i


def dec(shape, n):
    target = int("".join("1" for _ in range(shape)))
    a = get_certain_c(target, n)
    for i in range(shape):
        target_d = int("".join((lambda _: "1" if _ != i else "2")(_) for _ in range(shape)))
        b = get_certain_c(target_d, n)
        diff = get_diff(a, b)
        dd = int(a[diff]) - 1
        print(chr(ord('w') + diff), end="=")
        print(chr(ord('a') + i), end=" + %d" % dd)
        print()


def det_pos(shape, n):
    target = int("".join("1" for _ in range(shape)))
    a = get_certain_c(target, n)
    for i in range(shape):
        target_d = int("".join((lambda _: "1" if _ != i else "2")(_) for _ in range(shape)))
        b = get_certain_c(target_d, n)
        diff = get_diff(a, b)
        print(diff, end=" ")


if __name__ == '__main__':
    det_pos(20, 3)
