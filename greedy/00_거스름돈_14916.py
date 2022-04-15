import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
if N < 5:
    if N % 2 != 0:
        ans = -1
    else:
        ans = N // 2
else:
    ct, N = divmod(N, 5)
    if N == 0:
        ans = ct
    else:
        if N % 2 == 0:
            ct += N // 2
            ans = ct
        else:
            ct += (N + 5) // 2 - 1
            ans = ct
print(ans)