import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

def bfs(start):
	cnt = 1
	queue = deque([start]) #인자만큼 크기의 decue 생성
	visit = [False for _ in range(n+1)] # 방문을 확인하기 위한 visit 배열 생성
	visit[start] = True
	while queue:
		cur = queue.popleft()
		for nx in graph[cur]:
			if not visit[nx]:
				visit[nx] = True
				cnt += 1
				queue.append(nx)

	return cnt

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int,input().split())
	graph[b].append(a) #  신뢰하는 관계가 A, B 형태로 들어온다

maxCnt = 1
ans = []

for i in range(1,n+1):
	cnt = bfs(i) # bfs 안에 누적된 값을 확인한다.
	if cnt > maxCnt:
		maxCnt = cnt # 최댓 값을 누적한다.
		ans.clear() 
		ans.append(i) # 배열 안에 모든 값을 clear 한 후 누적한다.
	elif cnt == maxCnt: # 만약 누적된 값과 max 값이 일치하면 append 시킨다.
		ans.append(i)
print(*ans)

