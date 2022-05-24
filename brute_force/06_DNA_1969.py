import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
n, m = map(int, input().split())
s = []
result = ""
cnt = 0
for i in range(n):
    a = input()
    s.append(a.upper()) # 문자열에 string 넣기 >> 이차원 배열처럼 j열 i행 조회 가능
    print(s)
for i in range(m):
    a = [0 for i in range(26)] # 알파벳 크기 배열
    print(a)
    for j in range(n):
        a[ord(s[j][i]) - 65] += 1 # 해당 알파벳 index에 1을 더하라
    result += chr(a.index(max(a)) + 65) # 알파벳 index에 아스키코드를 통해 문자로 변환
for i in range(n):
    for j in range(m):
        if s[i][j] != result[j]:
            cnt += 1
print(result)
print(cnt)