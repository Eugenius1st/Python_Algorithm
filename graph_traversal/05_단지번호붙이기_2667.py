import sys
sys.stdin = open("input.txt", "rt")
from collections import deque

N = int(input())
graph = []
counts = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0]  
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))
  
  graph[x][y] = 0
  count = 1

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        count += 1
  
  counts.append(count) # 각 단지 카운트 수 증가

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      bfs(i, j)

counts.sort()
print(len(counts)) # 총 단지수

for i in counts:
  print(i) # 오름차순 된 단지수