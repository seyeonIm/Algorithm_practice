def solution(skill, skill_trees):
    answer = 0
    
    
     # 스킬문자 해당되는 애들 앞에 필수스킬 있는지 확인해야 하니깐 따로 스킬만 모아두는 리스트 만들어두자
    for skill_tree in skill_trees:
        p = 0
        dump = ""
        # 문자 하나끼리 비교
        for ch in skill_tree:
            if ch in skill: # 스킬 문자에 해당되면 집중조사
                dump+=ch # 검사를 위한 dump 추가 작업
        
        if dump == skill[:len(dump)]: # dump에서 이전 필수조건 거쳤는지 확인
                answer += 1
                

    return answer



