import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
cnt = 0
while N >=0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    N -= 3 # 5배수 될때까지 반복
    cnt += 1 # 개수 카운트
else:
    print(-1)