import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0
# 이는 가장 큰 수부터 나누어 남은 몫을 더하면 된다 !!
# 나누는 수가 나누어 지는 수보다 크다면 몫은 0이겠지.
# 그럼 for문만 돌려서 확인 가능하다
for i in reversed(arr):
    cnt += K // i
    K = K % i
    if K == 0:
        break
print(cnt)