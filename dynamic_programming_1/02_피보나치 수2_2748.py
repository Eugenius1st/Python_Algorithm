import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
res = 0

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    for i in range(N-1):
        tmp = st2 
        st2 = st1 + st2 
        st1 = tmp  
    print(st2)