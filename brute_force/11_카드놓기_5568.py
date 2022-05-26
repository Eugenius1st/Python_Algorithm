import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from itertools import permutations

n = int(input())
k = int(input())

arr = [input().rstrip() for _ in range(n)]

res = set()

print(arr)
for per in permutations(arr, k):
    
    res.add(''.join(per))
print(res)

print(len(res))