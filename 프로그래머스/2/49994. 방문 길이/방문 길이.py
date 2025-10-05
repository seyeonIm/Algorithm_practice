# 직관적사고: 일단 걸어온 길이를 구하려면 모든 좌표를 기록하고 기록한 개수를 세자. 이때 중복 제거하는데 중복이라는 건, 이동전좌표랑 이동후좌표가 반대방향일 때 포함해서 같아야 하는거네
# 구조화사고: 기록 딕셔너리 변수 하나 세워서 (이전좌표, 다음좌표)를 튜플이나 리스트로 묶어서 저장하고, 이때 set으로 같은방향 중복 없애고 sort로 반대방향 중복 없애자 그리고 개수 세면 되겠네

def solution(dirs):
    answer = 0
    x, y = 0, 0
    
    trace = set() 
    # trace = (edge, edge ..) # edge = [(이동전좌표),(이동후좌표)]
    move = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    
    for d in dirs:
        dx = move[d][0]
        dy = move[d][1]
        
        nx = x+dx
        ny = y+dy
        
        # 경계체크
        if nx<=5 and nx>=-5 and ny<=5 and ny>=-5:
            edge = tuple(sorted([(x,y), (nx,ny)]))
            trace.add(edge) 
            x, y = nx, ny
        
    print(trace) 
    answer = len(trace)
    
    
        
            
            
        
        

    
    return answer

# 명령어대로 캐릭터를 움직이면서, 이동한 좌표쌍을 튜플로 리스트나 set에 저장하고, 중복되지 않은 길만 세자
# 중복 길을 빼려면 이동 전/후 좌표쌍을 기록하자. 같은 길의 반대방향은 sorted로 같은 튜플로 만들고, 중복은 set이 막아준다. 단, 경계(-5~5) 안에서만 기록하고 마지막에 개수 세자

# 이때 if문으로 하면 복잡하니깐 이동은 딕셔너리로 정리하자