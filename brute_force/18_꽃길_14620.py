import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

flower = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]
N = int(input()) # 화단 한 변의 길이
board = [list(map(int,input().split())) for _ in range(N)] # N개의 줄에 N개씩 화단의 지점당 가격
visited = [[False]*N for _ in range(N)]
answer = 987654321

def check(y,x):
    global N
    for dy, dx in flower: #상하, 좌우, 중앙 확인
        ny = y + dy
        nx = x + dx
        if 0>ny or ny>N-1 or 0>nx or nx>N-1 or visited[ny][nx]: #visied는 boolean 타입
            return False
    return True

def calculate(y,x):
    global N
    result = 0
    for dy, dx in flower:
        ny = y + dy
        nx = x + dx
        result += board[ny][nx] #모든 합 result에 저장
    return result

def dfs(x, cost, cnt):
    global answer
    if cnt == 3: # 3개의 꽃 모두 다 놓았을 때 종료
        answer = min(answer, cost)
        return
    for i in range(x,N):#1부터 N까지 -> x부터 N까지
        for j in range(1,N):
            if check(i,j):
                visited[i][j] = True
                for dy,dx in flower:
                    visited[i+dy][j+dx] = True # 방문체크
                dfs(i, cost + calculate(i,j), cnt +1)
                visited[i][j] = False
                for dy,dx in flower:
                    visited[i+dy][j+ dx] = False
dfs(1,0,0)
print(answer)
