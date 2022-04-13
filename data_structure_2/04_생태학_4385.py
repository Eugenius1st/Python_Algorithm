import sys
sys.stdin = open("input.txt","rt")
def input():
    return sys.stdin.readline().rstrip()

dic = dict()
cnt = 0

while True:
    s = input()
    if s == "": 
        break
    cnt += 1
    if s in dic:
        dic[s] += 1
    else: 
        dic[s] = 1 #

dic = sorted(dic.items())

for val, key in dic:
    num = (key/cnt)*100.0
    if int(num) //2 ==0:
        num = num + 0.0005
    print(val, round(num, 4))