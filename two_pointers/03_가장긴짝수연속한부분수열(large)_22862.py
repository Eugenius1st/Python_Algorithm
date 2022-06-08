import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, k = map(int,input().split())
# k 번 삭제 가능
myList = list(map(int,input().split()))
lt = 0
rt = -1
ans = 0
odd = 0
temp = 0

while True:
    if odd <= k:
        ans = max(ans, temp-odd) # 유효한 상태
    if odd <= k: # 경계 조건 확인
        rt += 1
        if rt >= n:
            break
        if myList[rt] % 2 == 1:
            odd += 1
        temp += 1 # 유효한 상태
    else:
        if myList[lt] % 2 == 1:
            odd -= 1
        temp -= 1
        # 경계 조건 확인
        lt += 1
        if lt > rt :
            break
print(ans)