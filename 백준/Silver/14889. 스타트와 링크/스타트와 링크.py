# 

import sys
# Sij i+j, 차이 최소화

N = int(sys.stdin.readline())
S = []
team = [] # 조합 후 선수 포함한 팀 배열
min_diff = 10**9
for i in range(N):
    S.append(list(map(int, sys.stdin.readline().split())))
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0

# 1. 팀 나누기 = 조합
def dfs(idx, chosen_mem):
    global min_diff
    # 1. 기저 조건
    # 현재까지 구성된 스타트 팀(team)을 기준으로 링크 팀을 결정하고
        # 두 팀의 시너지 점수 합을 계산하여 그 차이를 min_diff와 비교, 갱신
    if chosen_mem == N//2:
        # 현재 팀(team)은 스타트 팀이 되고, 나머지 선수들은 링크 팀이 됨
        start_team = team[:]
        link_team = []
        for mem in range(N):
            if mem not in start_team:
                link_team.append(mem)

        # 두 팀의 시너지 점수 합 계산
        start_score = 0
        link_score = 0
        # 스타트 팀 내 모든 쌍에 대해 시너지 값 누적
        for i in range(len(start_team)): # 0,1
            for j in range(len(start_team)): #0,1
                start_score += S[start_team[i]][start_team[j]]
        # 링크팀 합
        for i in range(len(link_team)): 
            for j in range(len(link_team)): 
                link_score += S[link_team[i]][link_team[j]]

        # 차이
        diff = abs(start_score-link_score)
        if diff < min_diff:
            min_diff = diff 
        return # 최종 dfs 종료가 아닌 해당 분기에서 확장할 필요없다는 뜻

    
    # 2. 재귀 호출
    # for문을 통해 idx부터 N까지 반복하며, 각 선수 i를 선택("상태 업데이트")하고
        # dfs(i+1, cnt+1)을 호출하여 다음 선수 선택.
    # 재귀 호출 후에는 team에서 마지막에 추가했던 선수를 제거("백트래킹")하여 상태를 복구
    for i in range(idx, N):
        team.append(i)
        dfs(i+1, chosen_mem+1)
        team.pop() # 백트래킹: 마지막에 추가한 선수 i를 제거하여 상태 복구

dfs(0, 0) # 현재 인덱스(idx)=0 현재 고려중인 선수 번호, 선택된 선수 수(count)=0, 팀=[]
print(min_diff)