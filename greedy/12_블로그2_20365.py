import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
str = input()
red = 0
blue = 0

for i in range(N):
    if i == 0:
        if str[i] == 'R': red +=1
        if str[i] == 'B': blue += 1
    else:
        if str[i]=='R' and str[i-1]=='B':
            red+=1
        if str[i]=='B' and str[i-1]=='R':
            blue+=1

print(min(red,blue)+1)