import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dQ= deque()
move = list(input().split())
res = []

for i in range(N) :    
    dQ.append((i+1, move[i]))

for _ in range(N):
    tmp = dQ.popleft()
    idx = tmp[0]
    val = int(tmp[1])

    res.append(idx)
    if not dQ:
        break
    elif val > 0:
        for _ in range(val-1):
            dQ.append(dQ.popleft())

    elif val < 0 :
        cnt = -1
        for _ in range(val*(-1)):
             dQ.appendleft(dQ.pop())
            
for x in res:
    print(x, end=' ')
