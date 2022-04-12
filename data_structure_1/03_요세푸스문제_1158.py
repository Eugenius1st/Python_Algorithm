import sys
from collections import deque

n, k = map(int,input().split())
cnt = 0

dQ = list(range(1,n+1))
dQ = deque(dQ)
res = []

while dQ:
    cnt+=1
    tmp = dQ.popleft()
    if cnt==k:
        res.append(tmp)
        cnt = 0
    else:        
        dQ.append(tmp) 

print('<' + ', '.join(map(str, res)) + '>')