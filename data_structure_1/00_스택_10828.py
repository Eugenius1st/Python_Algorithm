import sys
sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
for i in range(N):
    cmd = input().split()

    if len(cmd) == 2:
        val = cmd[1] 
    cmd = cmd[0] 

    if cmd == "push":
        arr.append(val)

    elif cmd == "pop":
        print(arr.pop() if len(arr) else -1)

    elif cmd == "size":
        print(len(arr)) 

    elif cmd == "empty": #여기
        print(0 if len(arr) else 1)
 
    elif cmd == "top":
        print(arr[-1] if len(arr) else -1)
 