import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs():
    q = deque()
    q.append(1)

    while q:
        node = q.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                q.append(i)
        #print(parent)
    return parent

bfs()
for i in parent[2:]:
    print(i)