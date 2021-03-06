import sys
input = sys.stdin.readline
n,m = map(int,input().split())

result = [0]*10

def promising(result,i):
    switch = True
    for k in range(i):
        if result[k] == result[i] or result[i-1] > result[i]:
            switch = False
            break
    return switch

def nandm(i):
    if promising(result,i):
        if i==m:
            print(*[result[k] for k in range(1,m+1)])
        else:
            for j in range(i,n+1):
                result[i+1] = j
                nandm(i+1)

nandm(0)