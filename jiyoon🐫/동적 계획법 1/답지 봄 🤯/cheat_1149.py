import sys
input=sys.stdin.readline
n=int(input())
RGB=[]
for i in range(n):
    RGB.append(list(map(int,input().split())))

for i in range(1,n):
    print(i,end=' i\n')
    RGB[i][0]=min(RGB[i-1][1],RGB[i-1][2])+RGB[i][0]
    print(RGB[i][0])
    RGB[i][1]=min(RGB[i-1][0],RGB[i-1][2])+RGB[i][1]
    print(RGB[i][1])
    RGB[i][2]=min(RGB[i-1][0],RGB[i-1][1])+RGB[i][2]
    print(RGB[i][2])
    
print(min(RGB[n-1]))