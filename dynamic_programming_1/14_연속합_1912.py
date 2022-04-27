import sys
sys.stdin = open ("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*(len(arr))
dp[0] = max(0, arr[0])

for i in range(1,len(arr)):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))