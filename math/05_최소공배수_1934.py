import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

def lcm(a, b):
    return a * b / gcd(a, b)
    
for i in range(N):
    a, b = map(int,input().split())
    print(int(lcm(a,b)))