import sys
sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
cnt = 0
ch = [0]*(N)
for i in range(N):
    ch[i] = input()

for _ in range(M):
    s = input()
    if s in ch:
        cnt += 1
print(cnt)