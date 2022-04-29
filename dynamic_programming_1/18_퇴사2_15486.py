import sys
sys.stdin = open ("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
tv,pv = [],[]
dp = [0] * (n+1)

for i in range(n):
    x,y = map(int,input().split())
    tv.append(x)
    pv.append(y)

M = 0 
for i in range(n):
    M = max(M,dp[i])  
    if i+tv[i] > n :  
        continue 
    dp[i+tv[i]] = max(M+pv[i],dp[i+tv[i]])

print(max(dp))