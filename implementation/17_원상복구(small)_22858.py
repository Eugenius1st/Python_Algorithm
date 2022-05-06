import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline

n,k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))
length = len(d)

for _ in range(k):
    p = [0]*length
    for i in range(length):
        idx = d[i]
        p[idx-1] = s[i]
    s = p[:]
for j in p:
    print(j, end= ' ')