import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline


n, m = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(m):

    a, b, c = map(int,input().split())
    if a == 1:
        arr[b-1] = c
    else:
        if a == 2:
            for i in range(b-1,c):
                if arr[i] == 0:
                    arr [i] = 1
                else: arr[i] = 0
        elif a == 3:
            arr[b-1:c] = [0] * (c-b+1)
                # 전구를 모두 끈 상태인 0으로 만들어 준다
        else:
            arr[b-1:c] = [1] * (c-b+1)
                # 전구를 모두 켠 상태인 1로 만들어 준다
for i in arr:
    print(i, end=" ")