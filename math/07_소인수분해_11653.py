import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
tmp = N
while(True):
    if tmp == 1:
        break;    
    for i in range(2,N+1):
        if tmp % i == 0:
            print(i)
            tmp = tmp / i
            break