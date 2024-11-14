# 1924 (len(n)-k)개 추출 리스트
def solution(number, k):
    answer = [] 
    for num in number:
        if not answer:
            answer.append(num)
        if k > 0:  
            if answer[-1] < num:
                answer.pop()
                k -= 1
            if k <= 0 and not answer:
                break
        answer.append(num)
        
    if k > 0:
        answer = answer[:-k]
    else:
        answer
    return ' '.join(answer)
        
    
def solution(number, k):
    # 숫자 위치 변화하지 않은 상태에서 k개 빼는 것이 특별룰임
    # 스택에 쭉 넣다가 더 큰 숫자 넣으려고 하면 앞에 거 제거하고 넣기(정렬식) + 순회 후에도 k개수 다 못채웠으면 끝에 숫자 제거  
    answer = []
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)


## sol1 시간초과
# from itertools import combinations
# def solution(number, k):
#     answer = 0
#     c = combinations(list(number), len(number)-k)
#     result = [''.join(tp) for tp in list(c)]
#     print(result)
#     answer = max(result)
#     return answer