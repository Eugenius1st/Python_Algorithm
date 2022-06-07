import sys
sys.stdin = open("input.txt", "rt")
from collections import deque
# 폭탄 있는 칸은 3초 지난 후 폭발

def saveBomb():
    # 초기 좌표값 저장
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == 'O':
                remember.append((i,j))

def allBomb():
    # 폭탄 없는 모든 칸에 설치
    for i in range(R):
        for j in range(C):
            if bomb[i][j] == '.':
                bomb[i][j] = 'O'

def explode():
    # 3초 전에 설치한 폭탄 폭발
    # bombs deque에 들어있는 좌표로 폭탄 터트림
    while remember:
        y,x = remember.popleft()
        bomb[y][x] = '.'
        if 0 <= y-1:
            bomb[y-1][x] = '.'
        if 0 <= x-1:
            bomb[y][x-1] = '.'
        if y+1 < R:
            bomb[y+1][x] = '.'
        if x+1 < C:
            bomb[y][x+1] = '.'

if __name__ == "__main__":
    R, C, N = map(int,input().split())
    bomb = []
    remember = []
    for i in range(R):
        bomb.append(list(sys.stdin.readline().rstrip()))
        # string 은 끝에 \n있어서 rstrip로 읽어준다
    N -= 1
    while N:
        remember = deque()
        saveBomb()
        allBomb()
        N-=1
        if N ==0:
            break
        explode()
        N-=1

    for i in range(R):
        for j in range(C):
            print(bomb[i][j], end="")
        print()
