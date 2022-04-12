import sys
sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

standard = list(range(N,0,-1))
stack = []
res = []

for i in range(1,N+1):
    num = int(input())
    while standard or stack: # stack 이 비거나 standard가 비었을 경우
        if stack and stack[-1] == num: # stack의 끝값이 num일 경우
            stack.pop()
            res.append('-')
            break

        elif not stack or stack[-1] != num: # stack 이 비거나 stack의 끝 값이 num이 아닐 경우
            if not standard : #standard값이 비었을 경우
                print("NO")
                sys.exit()

            stack.append(standard.pop())
            res.append('+')

        else: 
            print("NO")
            sys.exit()
            
for x in res:
    print(x)
