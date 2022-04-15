import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []

for i in range(N):
    s, e = map(int,input().split())
    arr.append((s,e))
arr.sort(key = lambda x : (x[1],x[0]))
cnt = 1
std = arr[0][1]

for j in range(1,N):
    if std <= arr[j][0]:
        std = arr[j][1]
        cnt += 1
print(cnt)