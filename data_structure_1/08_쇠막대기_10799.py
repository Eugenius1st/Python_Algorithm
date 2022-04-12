import sys
sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

bracket = input()
cnt = 0
res = 0
 
for x in bracket:
    if x == '(':
        cnt +=1
    
    elif x==')':
        if before == ')':
            res += 1
            cnt -= 1
        else:         
            cnt -= 1
            res += cnt
    before = x
print(res)