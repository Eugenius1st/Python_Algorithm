import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline

def check_line():
    bingo = 0
    for i in range(5):
        bool1 = True
        bool2 = True
        for j in range(5):
            if board[j][i] != -1:
                bool1 = False
            if board[i][j] != -1:
                bool2 = False

        if bool1:
            bingo += 1
        if bool2:
            bingo += 1
    return bingo


def check_diagonal():
    bingo = 0
    bool1 = True
    bool2 = True
    for i in range(5):
        if board[i][i] != -1:
            bool1 = False
        if board[i][4-i] != -1:
            bool2 = False
    if bool1:
        bingo += 1
    if bool2:
        bingo += 1

    return bingo


dic = dict()
board = []
# 빙고판 만들기
for i in range(5):
    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    board.append(li)
    for j in range(5):
        dic[li[j]] = (i, j)


count = 0
flag = False
for _ in range(5):
    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    for each in li:
        count += 1
        r, c = dic[each]
        board[r][c] = -1

        if (check_diagonal() + check_line()) >= 3:
            print(count)
            flag = True
            break
    if flag:
        break