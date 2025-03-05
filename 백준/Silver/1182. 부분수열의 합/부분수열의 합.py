# 음수 섞여 있어서 투포인터X
# 부분합 => dfs + 백트랙킹

import sys
# 전역 변수 -> 함수 안에서 읽어서 사용할 수 있음
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
# 5 0
# -7 -3 -2 5 8
ans = 0

def dfs(idx, curr_sum): # 상태를 나타내는 변수들_현재위치,현재경로 또는 누적 상태, 추가정보(방문여부배열이나 현재 깊이 등)
    # global 선언이 없으면, DFS 함수 내에서 ans를 수정해도 그 수정된 값이 함수 밖으로 전달되지 않음
    # or 함수 인자로 넣던가
    global ans
    
    # 기저 조건 (종료 조건과 결과 처리)
    if idx == N: # 모든 원소 모두 고려
        if curr_sum == S:
            ans += 1
        return # 기저 조건에 도달했을 때 더 이상 재귀 호출 진행하지 않고 함수 종료
    
    # 재귀 호출
    dfs(idx+1, curr_sum + arr[idx]) # 현재 원소 선택 경우
    # 현재 원소 선택X 경우
    dfs(idx+1, curr_sum)

dfs(0,0)

if S == 0:
    ans -= 1
print(ans)


    