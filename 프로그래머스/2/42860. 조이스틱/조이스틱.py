def solution(name):
    # name = 'BNAAYAAAZ'
# 조이스틱 조작 횟수 
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 한 자리에서 알파벳 변경
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 커서 변경
        # i: 현재 커서의 위치
        next = i + 1
        # 현재 위치 i에서 오른쪽으로 가장 가까운 A가 아닌 알파벳의 인덱스
        # 즉, name 문자열에서 A가 아닌 알파벳을 만날 때까지 이동한 위치
        while next < len(name) and name[next] == 'A':
            # 사이 값 진행
            next += 1
        
        print('i:',i, 'next:',next)
        print('minmove:',min_move,'오왼넘',2*i + len(name) - next, '왼쭉:',i + 2 * (len(name) - next))
        min_move = min(min_move, 2 *i + len(name) - next, i + 2 * (len(name) - next))
        print('최종min_move:', min_move)

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    
    answer += min_move
    return answer
