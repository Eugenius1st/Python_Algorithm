import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

N , K = map(int,input().split())
K = str(K)
cnt = 0
#if else 로 00시간 형태를 맞춰주어야 한다. 
for h in range(N+1):
    if h<10:
        h = '0'+str(h)
    for m in range(60):
        if m<10:
            m = '0'+str(m)
        for s in range(60):
            if s<10:
                s = '0'+str(s)
            if K in str(h)+str(m)+str(s):
                cnt += 1
print(cnt)