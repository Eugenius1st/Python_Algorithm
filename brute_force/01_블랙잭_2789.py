import sys
sys.stdin = open("input.txt", "rt")

N,M = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
maxNum = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k] > M :
                continue
            else:
                result = arr[i]+arr[j]+arr[k]
                if maxNum <= result:
                    maxNum = result
print(maxNum)