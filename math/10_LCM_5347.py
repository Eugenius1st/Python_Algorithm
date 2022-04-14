import sys
sys.stdin = open("input.txt","rt")
from math import lcm    
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

def gcd(a, b): # 최대공약수
    a, b = max(a, b), min(a, b)
    while b != 0:
        a,b = b, a % b
    return a
def lcm(a, b): # 최소공배수
  return int(a * b / gcd(a, b))

for i in range(N):
    
    a, b = map(int,input().split())

    print(lcm(a,b))