import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
like = [list(map(int, input().split())) for _ in range(n)]

maxSum = 0
for a, b, c in combinations(range(m), 3):
    # 0부터 5까지, 3개 조합
    tmpSum = 0
    for i in range(n):
        # 0 부터 4
        # a , b , c 라는 조합을 골라서 max값을 누적한다
        tmpSum += max(like[i][a], like[i][b], like[i][c])
    maxSum = max(maxSum, tmpSum)

print(maxSum)