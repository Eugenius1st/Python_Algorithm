import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
sumNum = 0
stdNum = 0

for i in range(1,N+1):
    sumNum = i
    stdNum = str(i)
    for j in stdNum:
        sumNum += int(j)
    if sumNum == N:
        print(i)
        exit()
else:
    print(0)