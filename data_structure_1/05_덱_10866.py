import sys
sys.stdin = open("input.txt", "rt")
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def push_front(X):
    arr.appendleft(X )
def push_back(X):
    arr.append(X)
def pop_front():
    print(arr.popleft() if len(arr) else -1)
def pop_back():
    print(arr.pop() if len(arr) else -1)
def size():
    print(len(arr))
def empty():
    print(0 if len(arr) else 1)
def front():
    print(arr[0] if len(arr) else -1)
def back():
    print(arr[-1] if len(arr) else -1)

N = int(input())
arr = deque([])

for i in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        val = cmd[1]
    cmd = cmd[0]

    if cmd == "push_front":
        push_front(val)

    elif cmd == "push_back":
        push_back(val)

    elif cmd == "pop_front":
        pop_front()

    elif cmd == "pop_back":
        pop_back()

    elif cmd == "size":
        size()

    elif cmd == "empty":
        empty()

    elif cmd == "front":
        front()

    elif cmd == "back":
        back()