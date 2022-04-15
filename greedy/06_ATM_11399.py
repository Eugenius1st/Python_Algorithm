import sys

def input():
    return sys.stdin.readline().rstrip()
# 3 1 4 3 2
# 1 2 3 3 4

N = int(input())
arr = list(map(int,input().split()))
res = 0
accu = 0
arr.sort()

for x in arr:
    accu += x
    res += accu
print(res)