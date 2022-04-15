import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()


A, B = input().split()
cnt = 1

while B != A:
    #같아지려는 수보다 작아진 경우
    if int(B) < int(A):
        print(-1)
        exit()

    elif int(B[-1]) == 1:
        cnt+=1
        # 맨 뒤 값 뺀 수로 초기화
        B = B[:len(B)-1]

    elif int(B) % 2 == 0:
        cnt+=1
        B = str(int(B) // 2)
    
    else:
        print(-1)
        exit()

print(cnt)