import sys
sys.stdin = open("input.txt", "rt")
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(range(1,N+1))
arr = deque(arr)

while len(arr) != 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])