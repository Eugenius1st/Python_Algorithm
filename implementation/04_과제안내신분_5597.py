import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline

# 입력은 28줄
res = [0]*30

for i in range(28):
    n = int(input())
    res[n-1] = 1

for i in range(len(res)):
    if res[i] == 0:
        print(i+1)