import sys
sys.stdin = open("input.txt","rt")

def input():
    return sys.stdin.readline().rstrip()
    
subNum = input().split('-') # '+' 기준으로 나누어 원소 저장 5-5+4 라면 '5' '5+4' 로 저장
cal = []

for i in subNum:
    val = 0
    plusNum=i.split('+')
    for j in plusNum:
        val+=int(j)
    cal.append(val)
stdNum = cal[0]

for j in range(1,len(cal)):
    stdNum -= cal[j]
print(stdNum)