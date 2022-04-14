import sys
sys.stdin = open("input.txt","rt")
def input():
    return sys.stdin.readline().rstrip()

def gcd(a, b):
    if b == 0:
        return a;
    return gcd(b, a % b);
N = int(input())
while(N):
    N = N-1
    res = 0
    arr = list(map(int,input().split()))
    print(arr)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(i, j)
            res += gcd(arr[i], arr[j]);
            print(res)
            
    print(res)