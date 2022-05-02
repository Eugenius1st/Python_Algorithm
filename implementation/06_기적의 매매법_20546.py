import sys
sys.stdin = open ("input.txt", "rt")
input = sys.stdin.readline

# 14일에 각자 주식 비교
n = int(input())
stock = list(map(int,input().split()))
jh, jhM = n, 0
sm, smM = n, 0
smArr = [] # 상승과 하락 확인

for x in stock:
    #BNF
    jhM += jh // x
    jh = jh % x #남은 돈
    #TIMING
    smArr.append(x)
    if len(smArr) >=4:
        if smArr[0] > smArr[1] > smArr[2]:
            smM += sm // x
            sm = sm % x
        elif smArr[0] < smArr[1] < smArr[2]:
            sm += smM*x
            smM = 0
        smArr.pop(0) # 맨 앞의 수 제거(len을 4로 유지)

if jh + stock[-1]*jhM > sm + stock[-1]*smM:
    #print(jh + stock[-1]*jhM , sm + stock[-1]*smM)
    print('BNP')
elif jh + stock[-1]*jhM < sm + stock[-1]*smM:
    #print(jh + stock[-1]*jhM , sm + stock[-1]*smM)
    print('TIMING')
else:
    print('SAMESAME')