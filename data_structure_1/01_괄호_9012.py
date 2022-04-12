import sys
sys.stdin = open("input.txt", "rt")


def input():
    return sys.stdin.readline().rstrip()

N = int(input())
res = 0

for i in range(N):
    PS = input()
    arr=[]

    val = 0
    for x in PS:        
        if x == "(":
            arr.append("(")
        else :
            if len(arr)==0:
                val=-1
                break
            arr.pop()

    if val == 0:
        if len(arr) == 0:
            print("YES")    
        else:
            print("NO")
    else: print("NO")