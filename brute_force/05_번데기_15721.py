import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
A = int(input()) # 게임을 진행하는 사람 수 A명
T = int(input()) # 구하고자 하는 T 번째
N = int(input()) # 구하고자 하는 구호
arr = []
re = 0
bun = deggi = 1
while True:
    preRe = bun
    re+=1
    for _ in range(2):
        arr.append((bun, 0))
        bun += 1
        arr.append((deggi, 1))
        deggi += 1
    for _ in range(re+1):
        arr.append((bun, 0))
        bun+=1
    for _ in range(re+1):
        arr.append((deggi,1))
        deggi += 1
    if preRe < T <=bun:
        print(arr.index((T, N)) % A)
        break