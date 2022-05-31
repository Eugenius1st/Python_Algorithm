import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# dynamic programming 기법을 사용하여 문제를 해결합니다.
# 문제의 뒤에서 부터 접근을 하여 공식을 만들어 보자면
# N번째 날은 N+1번째 날 기준 수익(dp)과 N번째 날 수익 + Tn 만큼 지난 후 수익(dp)중 큰 값

N = int(input())

timeTable = [list(map(int,input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N-1,-1,-1):
   
    if i + timeTable[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])    