import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n= int(input()) #정점
m = int(input()) #연결수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited_dfs = []
print(graph)
 
def dfs(graph, cur_node, visited):
    # 현재 노드를 방문처리
    visited.append(cur_node)
    graph[cur_node].sort()
    # 현재 노드와 인접한 노드를 확인
    for link_node in graph[cur_node]:
        print(link_node, visited)
        # 방문하지 않은 노드라면 재귀호출
        if link_node not in visited:           
            dfs(graph, link_node, visited)
dfs(graph, 1, visited_dfs)

print(len(visited_dfs)-1)