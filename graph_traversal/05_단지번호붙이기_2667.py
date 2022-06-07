import sys
sys.stdin = open("input.txt", "rt")
from collections import deque

N = int(input())
graph = []
counts = []
for _ in range(N):
    graph.append(list(map(int,input())))

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0 # 0으로 초기화
    cnt = 1 # 단지 내 집 수 카운팅
 
    while queue:
        x,y = queue.popleft() # queue에서 기준 좌표 꺼낸다
        for i in range(4): # 상, 하, 좌, 우 확인
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1: #graph 값이 1이면
                graph[nx][ny] = 0     # 0으로 초기화            
                queue.append((nx,ny)) # 상하좌우 확인 위해 queue에 append 한다
                cnt +=1
    counts.append(cnt) #단지 수들을 몹는다

for i in range(N):
    for j in range(N): # 2중 for문으로 2차원 배열을 돌며 1 확인한다
        if graph[i][j] == 1:
            bfs(i,j)
counts.sort()
print(len(counts))

for i in counts:
    print(i)