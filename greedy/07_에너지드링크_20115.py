import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
res = arr[0]

for i in range(1,N):
    res += arr[i]/2

print(res)