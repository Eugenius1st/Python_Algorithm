import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
res = [-1]*(n+1)
cnt = 0
for i in range(n):
    a, b = map(int,input().split())
    if res[a] == -1:
        res[a] = b
    elif res[a] != b:
        cnt += 1
        res[a] = b

print(cnt)