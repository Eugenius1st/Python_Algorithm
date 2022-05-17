import sys
sys.stdin = open("input.txt", "rt")

# A B C M
# 피로도 쌓, 일처리 정도, 피로도 줄, 제한 피로도
A, B, C, M = map(int,input().split())
day = 24
# 하루(24)에 최대 할 수 있는 일을 구하여라
# 10넘기면 안됌.. -> 5 넘기면 안됌
stress = 0 # 누적 피로도
work = 0 # 누적 일
check = 0 # 누적 시간

if A > M :
    print(0)
    exit()

else:
    while day != check:
        if stress + A <= M:
            stress += A
            work += B
            check += 1
        else:
            stress -= C
            check += 1
            if stress < 0:
                stress = 0
print(work)
