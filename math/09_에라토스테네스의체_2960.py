import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()
    
N,K = map(int,input().split())
arr = [0] * (N+1)
cnt = 0

for i in range(2,N+1):
    if arr[i] == 0:
        for j in range(i, N+1, i):
            if arr[j]==0:
                arr[j] = 1
                cnt += 1
                if cnt == K:
                    print(j)
                    exit()