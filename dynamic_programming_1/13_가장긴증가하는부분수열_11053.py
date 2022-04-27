import sys
sys.stdin = open ("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*(len(arr))

for i in range(n):
    for j in range(i):
        if dp[i] < dp[j] and arr[i] > arr[j]:
            dp[i] = dp[j]
    dp[i]+=1
print(dp)