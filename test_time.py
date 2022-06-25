import time
import subprocess

if __name__ == '__main__':
    targets = [1000000000000000000000000000000000000000000000000]
    try_time = 100
    for target in targets:
        time_con = 0
        for i in range(try_time):
            proc = subprocess.Popen('toy_lock.exe l', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            time_con -= time.time_ns()
            proc.communicate(input=('%s\n' % str(target)).encode())
            time_con += time.time_ns()
        time_con = time_con / try_time
        print('%d, %s' % (target, format(time_con, ',')))
