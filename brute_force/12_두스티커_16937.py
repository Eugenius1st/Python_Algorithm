import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline

def isFeasible(r1, c1, r2, c2):
# 주어진 두 스티커를 놓을 수 있으면 true 를 반환, 그 외 false 를 반환
# 회전 여부가 결정된 상태 
    if (r1+r2 <= H and max(c1,c2) <= W): return True
    if (max(r1,r2) <= H and c1+c2 <= W): return True
    return False

def isPossible(r1, c1, r2, c2):
# 주어진 두 스티커를 놓을 수 있으면 true 를 반환, 그 외 false 를 반환 
# 회전 여부는 고려되지 않은 상태
    if (isFeasible(r1, c1, r2, c2)): return True # (안회전, 안회전) 
    if (isFeasible(c1, r1, r2, c2)): return True # (회전, 안회전) 
    if (isFeasible(r1, c1, c2, r2)): return True # (안회전, 회전) 
    if (isFeasible(c1, r1, c2, r2)): return True # (회전, 회전) 
    return False

if __name__ == "__main__":
    H, W = map(int,input().split()) 
    N = int(input())
    R = [0]*N 
    C = [0]*N
    for i in range(N): 
        R[i], C[i] = map(int,input().split())
    ans = 0;
    for i in range(N):
        for j in range(i+1,N):
            r1 = R[i]
            c1 = C[i] # 스티커 1 
            r2 = R[j]
            c2 = C[j] # 스티커 2 
            if (isPossible(r1, c1, r2, c2)): # 놓을 수 있으면 
                ans = max(ans, r1*c1 + r2*c2) # 답을 갱신 
    print(ans)

