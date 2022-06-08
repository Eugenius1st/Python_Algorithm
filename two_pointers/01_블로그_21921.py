import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

n, x = map(int, input().split())  # 블로그 일수, x일 동안 가장 많이 들어온 방문자
blog = list(map(int, input().split()))

if max(blog) == 0:
    print("SAD")
else:
    # pre는 누적 방문자 수
    pre = [0]
    for i, a in enumerate(blog):
        pre.append(pre[i] + a)

    lt = 0
    rt = x
    res = 0
    cnt = 0

    while rt <= n:
        if rt - lt == x:
            if res < pre[rt] - pre[lt]:
                res = pre[rt] - pre[lt]
                cnt = 1
            elif res == pre[rt] - pre[lt]:
                cnt += 1
            lt += 1
            rt += 1

    print(res)
    print(cnt)