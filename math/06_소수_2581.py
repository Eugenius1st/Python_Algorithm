import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()

a =int(input()) 
b =int(input()) 

N = max(a,b)
sum = 0

res = [0]*(N+1)
arr= [0]*(N+1)
minNum = 2147000000
for i in range(2,b+1):
    if arr[i]==0:
        res[i] = i
        for j in range(i,N+1,i):
            arr[j] = 1

res = res[min(a,b):max(a,b)+1]
if max(res) == 0:
    print(-1)
    exit()

for x in res:
    if x != 0:
        sum += x
        if x < minNum:
            minNum = x
print(sum)
print(minNum)