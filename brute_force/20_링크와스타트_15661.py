import sys
sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline
# 두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.!! 이 부분 해결 어려움
# start 팀을 선택하거나 선택하지 않으면서 집합을 구성한다
# 각 경우의 수에 대해 능력치 차이를 계산한다
# 가장 작은 차이를 출력한다
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def go(index, start, link) : 
  if index == n :
    if len(start) == n or len(link) == n :
      return -1
    
    team_start = 0
    team_link = 0

    for i in range(len(start)) :
      for j in range(i+1, len(start)) :
        if i == j : continue
        team_start = team_start + s[start[i]][start[j]] + s[start[j]][start[i]]
    
    for i in range(len(link)) :
      for j in range(i+1, len(link)) :
        if i == j : continue
        team_link = team_link + s[link[i]][link[j]] + s[link[j]][link[i]]

    diff = abs(team_start - team_link)
    return diff
  
  if len(start) > n or len(link) > n : return -1

  ans = -1

	# index의 사람을 start 팀에 넣었을 때
  team_start = go(index+1, start+[index], link)
  if ans == -1 or (team_start != -1 and ans > team_start) :
    ans = team_start
  
	# index의 사람을 link 팀에 넣었을 때
  team_link = go(index+1, start, link+[index])
  if ans == -1 or (team_link != -1 and ans > team_link) :
    ans = team_link

  return ans

print(go(0,[],[]))
