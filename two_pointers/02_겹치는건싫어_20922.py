import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# 같은 정수를 x개 이하로 포함한 최장 연속 부분 수열의 길이 구하기
n, x = map(int, input().split())  
# n개의 길이 x개의 같은 정수
hongdae = list(map(int, input().split()))
counter = [0] * (max(hongdae)+1)
lt = 0
rt = 0
res = 0

while rt < n :
    if counter[hongdae[rt]] < x:
        counter[hongdae[rt]] += 1
        rt += 1
    else:
        counter[hongdae[lt]] -= 1
        lt += 1
    res = max(res, rt - lt)
print(res)