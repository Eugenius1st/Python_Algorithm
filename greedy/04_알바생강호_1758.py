n=int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True) # 역순 정렬
sum = 0

for i in range(n):
    if arr[i] - i < 0: # 음수일 경우
        continue
    sum += (arr[i])-i
print(sum)