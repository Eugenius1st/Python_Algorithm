import sys
sys.stdin = open ("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
res = 0

dp = [[0] * n for _ in range(n)]  # i,j까지 올 수 있는 경우의 수를 저장
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:  # 끝에 도달했을 때
            print(dp[n-1][n-1])

            break
        cur = field[i][j]
        if j + cur < n:
            dp[i][j + cur] += dp[i][j]
        # 아래로 가기
        if i + cur < n:
            dp[i + cur][j] += dp[i][j]
