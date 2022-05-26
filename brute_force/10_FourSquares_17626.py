import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n = int(input())
dp = [0,1]

for i in range(2,n+1):
    minVal = 1e9
    j = 1
    while(j**2) <= i:
        minVal = min(minVal, dp[i-(j**1)])
        j += 1
    dp.append(minVal)
print(dp[n])