import sys
sys.stdin = open("input.txt","rt")
import math
def input():
    return sys.stdin.readline().rstrip()

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    strX = str(x)
    for j in range(len(strX)//2):
        if strX[j] != strX[-j -1]:
            return False
    else:
        return True


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        N = N+1
    while(True):
        if isPrime(N):
            if isPalindrome(N):
                break
        N = N+1
    print(N)