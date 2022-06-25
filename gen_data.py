import os
import subprocess
import time

if __name__ == '__main__':
    if os.path.exists('data.csv'):
        with open('data.csv', 'r') as file:
            start = file.readlines()
            start = len(start)
    else:
        start = 0
    data = []
    while True:
        for i in range(0, 1000):
            proc = subprocess.Popen('toy_lock.exe l', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            ret = proc.communicate(input=('%s\n' % str(start)).encode())
            ret = ret[0].decode()
            data.append(str(start) + "," + ret)
            start += 1
        with open('data.csv', 'a') as file:
            for d in data:
                file.write(d)
            data = []
            print('Done Once,%d, %d' % (start, int(time.time())))
