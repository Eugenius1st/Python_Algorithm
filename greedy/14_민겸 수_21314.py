import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

minRes = []
maxRes = []
cnt = 0
str = input()
for i in range(len(str)):
    if str[i] == 'M':
        cnt += 1
    elif str[i] == 'K':
        if cnt == 0:
            minRes.append(5)
            maxRes.append(5)
        else:
            minRes.append(10**(cnt-1))
            minRes.append(5)
            maxRes.append(5*10**(cnt))
            cnt = 0
if cnt > 0:
    minRes.append(10**(cnt-1))
    for _ in range(cnt):
        maxRes.append(1)

for x in maxRes:
    print(x,end='')
print()

for x in minRes:
    print(x,end='')