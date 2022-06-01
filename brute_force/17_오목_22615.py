import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# 가로줄 번호와 세로줄 번호 순서대로 출력

board = []
for i in range(19):
    board.append(list(map(int,input().split())))

dx = [0,1,1,-1]
dy = [1,0,1,1]
stdN = 19
for x in range(stdN):
    for y in range(stdN):
        if board[x][y] != 0:
            # 0아닌 경우 즉, 2이거나 1인경우 for 문을 돌려 위, 아래, 대각선 위, 대각선 아래 확인
            focus = board[x][y]

            for i in range(4):
                cnt = 1
                nx = x+dx[i]
                ny = y+dy[i]

                while 0 <= nx < 19 and 0 <=ny < 19 and board[nx][ny] == focus:
                    cnt += 1
                    if cnt == 5:
                        if 0 <=x - dx[i] <19 and 0 <= y - dy[i] < 19 and board[x-dx[i]][y - dy[i]] == focus:
                            break
                        if 0<= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx+dx[i]][ny + dy[i]] == focus:
                            break
                        # 육목이 아니면 성공한거니 종료
                        print(focus)
                        print(x+1, y+1)
                        sys.exit(0)
                    nx += dx[i]
                    ny += dy[i]
print(0)