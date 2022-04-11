import sys

sys.stdin=open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
res = [0]*(N+1)
res[1] = 1
maxLen = 0

for i in range(2,N+1): # 마지막 값이 i 라고 생각하고 도는 for문
    max = 0
    for j in range(i-1,0,-1): # i 보다 앞의 값을 비교하는 for문
        if arr[i]>arr[j] and res[j] > max:
            max = res[j]
        res[i] = max + 1
    if res[i] > maxLen: # 최대 수열 초기화
        maxLen = res[i]
print(maxLen)