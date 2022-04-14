import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

def isPrime(x):
    if x < 2: 
        return False;
    for i in range (2,x):
        if x % i == 0:
           return False;
    return True;

while(N):
    N = N-1
    std = int(input())
    while(not isPrime(std)):
        std += 1
    print(std)