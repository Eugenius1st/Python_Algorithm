import sys
sys.stdin = open("input.txt", "rt")

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
calStr = input()
calOper = '+-/*'
arr = []
num = []
dict = {}


for i in range(N):
    num.append(int(input()))
num.reverse()
# 이렇게만 끝내면 안되고, deque와 딕셔너리를 이용해야 했다!!
for i in calStr:
    if i not in dict and i not in calOper:
        dict[i] = num.pop()
print(dict)

for i in range(len(calStr)):
    if calStr[i] == '+':
        tmp1 = arr.pop()
        tmp2 = arr.pop()
        arr.append(tmp2+tmp1)   

    elif calStr[i] == '-':
        tmp1 = arr.pop()
        tmp2 = arr.pop()
        arr.append(tmp2-tmp1)

    elif calStr[i] == '*': 
        tmp1 = arr.pop()
        tmp2 = arr.pop()
        arr.append(tmp2*tmp1)

    elif calStr[i] == '/':
        tmp1 = arr.pop()
        tmp2 = arr.pop()
        arr.append(tmp2 / tmp1)
    else:
        arr.append(dict[calStr[i]])
        # 딕셔너리 값은 이렇게 키값을 넣어 value를 찾는다.

res = float(arr[0])
print("%.2f"%res)