import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

n = int(input()) 
ans=0 
a = list(map(int,input().split())) 
s=[] 
s.append(a[0])

for i in range(1,n): 
    s.append(s[i-1]+a[i]) 
    # s라는 배열에 각 자리에 누적 합을 구한다.

for i in range(1,n-1): 
    ans=max(ans,s[n-2]-a[0]+a[i]) 
    # 꿀이 맨 오른쪽에 위치했을 경우 가장 큰 값을 계산한다.

for i in range(1, n - 2): 
    ans = max(ans, s[n-1] - a[0] - a[i] + s[n-1] - s[i]) 
    # 꿀이 맨 오른쪽에 위치했을 경우 가장 큰 값을 계산한다.

for i in range(1,n-1): 
    ans=max(ans,2*s[i-1]+s[n-2]-s[i]) 
    print(ans)
    # 꿀이 사이에 있는 경우 가장 큰 값을 계산한다.

print(ans)