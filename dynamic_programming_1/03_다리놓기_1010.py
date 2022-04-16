import sys

sys.stdin=open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

def factorial(x):
    tmp = 1
    for i in range(1,x+1):
        tmp *= i
    return tmp

Re = int(input())
res = 0
for _ in range(Re):
    N, M = map(int,input().split())
    res = factorial(M) // (factorial(N) * factorial(M-N))
    print(res)