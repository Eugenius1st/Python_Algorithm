import sys
sys.stdin = open("input.txt","rt")
import math
def input():
    return sys.stdin.readline().rstrip()

# 소수 판별
# 이 부분에서 시간초과
def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
        if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
            return False# 전부 나눠떨어지지 않는다면 소수임
    return True
#1 x 8 = 8
#2 x 4 = 8
#4 x 2 = 8
#8 x 1 = 8
#앞서 말했듯, 1과 자기자신을 제외한 약수가 존재하는지 확인하려면, 자기자신의 제곱근(루트)까지만 확인하면 된다.
#어차피 약수들이 대칭적으로 짝을 이뤄서 8을 완성하기 때문이다.
#루트8은 약 2.8정도이므로 자연수 2까지만 확인해서 8에 나눠떨어지는지 확인하면 된다.

def multifly(listA):
    listA = set(listA) # 중복 제거
    res = 1
    for x in listA:
        res *= x
    return res

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    prime = []

    for i in range(N):
        if primenumber(arr[i]):
            prime.append(arr[i])
    
    if len(prime) == 0:
        print(-1)
        exit()

    print(multifly(prime))    