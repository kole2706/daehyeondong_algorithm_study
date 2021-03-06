# counting sort
import sys

n = int(sys.stdin.readline())
c = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    c[num] += 1

for i in range(10001):
    if c[i] != 0:
        for _ in range(c[i]):
            print(i)
