import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
from itertools import permutations
# 동일한 위치면 스트라이크
# 숫자는 같으나 다른 자리에 위치하면 볼
N = int(input()) # 미리 순열에 넣어둔다
arr = list(permutations([1,2,3,4,5,6,7,8,9], 3)) # 중복x 순서o
for _ in range(N):
    test, a, b = map(int,input().split())
    test = list(str(test))
    # test와 arr값을 대조해본다.
    remove_cnt = 0

    for i in range(len(arr)):
        s_cnt = b_cnt = 0
        i -= remove_cnt
        for j in range(3):
            test[j] = int(test[j])
            if test[j] in arr[i]: # 입력받은 수가 arr에 있는지 하나하나 확인
                if j == arr[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1

        if s_cnt != a or b_cnt != b:
            arr.remove(arr[i])
            remove_cnt += 1
            # 입력받은 스트라이크와 볼 개수가 같은지 확인하고, 다르면 remove 한다
print(len(arr))