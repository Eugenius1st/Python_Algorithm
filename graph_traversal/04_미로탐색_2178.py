import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# 초기 입력값 받기
import sys
input = sys.stdin.readline
N,M = map(int, input().split(" "))

G = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    x = list(input())
    for j in range(M):
        G[i][j] = int(x[j])

# 방문여부/회차 저장
visited = [[0]*M for i in range(N)]
# 상하/좌우 탐색
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 시작지점 넣기
queue = [(0,0)]
visited[0][0] = 1


while queue:
    x,y = queue.pop(0)

    if x == N-1 and y == M-1:
    	# 목적지 도착하면 break
        print(visited[x][y])
        break
	
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 그래프 내부인 경우만 탐색
        if (0 <= nx < N) and (0 <= ny <M):
        	# 방문한적 없고, 그래프 경로가 연결된 경우 
            #queue에 저장하고, visited는 이전 visited된 노드갯수 +1 업데이트
            if(visited[nx][ny]==0 and G[nx][ny]==1):
                visited[nx][ny] = visited[x][y]+1
                queue.append((nx,ny))