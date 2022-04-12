import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
pocket = dict()

for i in range(1,N+1):
    name = input()
    pocket[i] = name
reverse_pocket = dict(map(reversed,pocket.items()))

for x in range(M):
    search = input()
    if search.isdigit():
        print(pocket[int(search)])
    else:
        print(reverse_pocket[search])