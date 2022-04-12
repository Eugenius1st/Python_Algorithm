import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

Re = int(input())

for i in range(Re):
    N, M = map(int,input().split()) # 문서 개수, 원하는 문서 위치
    arr= list(map(int,input().split())) # 리스트 받음
    indexDQ = deque()
    primaryDQ = deque()
    cnt = 0

    for j in range(N):
        indexDQ.append(j)
        primaryDQ.append(arr[j])
    
    while indexDQ:
        maxNum = max(primaryDQ)

        if maxNum == primaryDQ[0]:            
            if M == indexDQ[0]:
                cnt+=1
                print(cnt)
                break
            else:
                cnt+=1
                indexDQ.popleft()
                primaryDQ.popleft()
                
        else:
            indexDQ.append(indexDQ.popleft())
            primaryDQ.append(primaryDQ.popleft())