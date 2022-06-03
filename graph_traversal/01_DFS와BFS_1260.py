import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from collections import deque

def bfs(x): 
    q = deque()
    q.append(x)
    visitedG[x] = 1
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if visitedG[i] == 0 and graph[v][i]==1:
                q.append(i)
                visitedG[i] = 1
def dfs(v):
  visitedG2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visitedG2[i] == 0 and graph[v][i] == 1:
      dfs(i)

if __name__ == "__main__":
    n,m,v = map(int,input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    visitedG = [0]*(n+1)
    visitedG2 = [0]*(n+1)

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a][b] = graph[b][a] = 1

    dfs(v)
    print()
    bfs(v)