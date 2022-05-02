import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline

n= int(input())

for i in range(n):
    maxNum = -1e9
    minNum = 1e9
    m = int(input())
    arr = list(map(int,input().split()))

    for x in arr:
        if x > maxNum:
            maxNum = x
        if x < minNum:
            minNum = x
    print( minNum, maxNum)