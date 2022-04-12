import sys
sys.stdin = open("input.txt", "rt")
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
arr = deque(arr)

def push(val):
    arr.append(int(val))

def pop():
    print(arr.popleft() if len(arr) else -1)

def size():
    print(len(arr))

def empty():
    print(0 if len(arr) else 1)

def front():
    print(arr[0] if len(arr) else -1)


def back():
    print(arr[-1] if len(arr) else -1)


for i in range(N):

    cmd = input().split()

    if len(cmd) == 2:
        val = cmd[1]
    cmd = cmd[0]

    if cmd == "push":
        push(val)
    elif cmd == "pop":
        pop()
    elif cmd == "size":
        size()
    elif cmd == "empty":
        empty()
    elif cmd == "front":
        front()
    elif cmd == "back":
        back()