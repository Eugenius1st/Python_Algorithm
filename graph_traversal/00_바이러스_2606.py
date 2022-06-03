import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 방문한 노드 누적

visitedG = []

def dfs(graph, curNode, visitedG):
    visitedG.append(curNode)
    # 현재 노드 방문처리
    graph[curNode].sort()
    # 인접한 노드 확인
    for linkedNode in graph[curNode]:
        # print(linkedNode, visitedG)
        # 방문하지 않은 노드라면 재귀 호출
        if linkedNode not in visitedG:
            dfs(graph, linkedNode, visitedG)

dfs(graph, 1, visitedG)
print(len(visitedG)-1)
