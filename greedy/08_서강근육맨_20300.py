import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))
res = []

arr.sort()

if len(arr)%2 == 0:
    for i in range(len(arr)//2):
        res.append(arr[i]+arr[-i -1])
    print(max(res))
else:
    res.append(arr[-1])
    for i in range(len(arr)//2):
        res.append(arr[i]+arr[-i -2])
    print(max(res))