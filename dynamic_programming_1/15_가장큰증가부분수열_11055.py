import sys
sys.stdin = open ("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*(n)
dp[0] = arr[0]

for i in range(n):
    sum = 0
    for j in range(0,i):    
        if arr[j]<arr[i] :       
            dp[i] = max(dp[i],dp[j]+arr[i])
        else:
            dp[i] = max(dp[i], arr[i])
print(max(dp))