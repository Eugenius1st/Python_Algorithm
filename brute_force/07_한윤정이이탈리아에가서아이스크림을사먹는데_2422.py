import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, m = map(int,input().split())
# n은 아이스크림 종류, m은 조합 개수
# 3가지 아이스크림을 선택해야 한다.
iceCream = n*(n-1)*(n-2) // 6
ch = [set() for _ in range(n)]
# set 함수는 "중복 삭제 기능" 
# set에 값 추가할때는 add 명령어 사용, 여러개 값을 추가할때는 update 명령어 사용

for i in range(m): # 리스트에 각 맛 별로 조합이 좋지 않은 맛을 넣는다.
    a, b = map(int,input().split())
    iceCream -= (n-2) - len(ch[a-1] | ch[b-1])
    # 2가지가 정해진 상황에서, 나머지 한가지 맛을 고르는 경우의 수는 n-2이다.
    # 그 전의 경우의 수에서 없앤 경우의 수는 합집합의 길이가 된다.
    ch[a-1].add(b)
    ch[b-1].add(a)
    print(ch)
print(iceCream)