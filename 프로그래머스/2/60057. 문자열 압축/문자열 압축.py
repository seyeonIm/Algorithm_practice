# 같은 값 연속해서 나타나는 것 
# -> 해당 문자 개수(여러 문자 단위 가능) + 해당 문자
# n의 크기가 크지 않을 때는 완전 탐색이 가능한지 가장 먼저 고려
# 문자열을 특정 구간만큼 건너뛰어 접근해야 할 때는 for 문의 3번째 파라미터 이용
# 완전탐색

# 문자열을 1개 단위부터 절반 길이까지 모든 가능한 단위로 자르는 시도
    # 1개씩 다 잘랐을 때 압축하고 2개씩 다 잘랐을 때 압축하고
# 각 단위로 문자열을 압축했을 때의 길이를 계산
# 가장 짧은 압축 길이를 찾아 반환



def solution(s):
    answer = [len(s)]  # 압축하지 않은 원본 문자열 길이로 초기화

    # 1부터 문자열 길이의 절반까지 모든 가능한 단위로 압축 시도
    for i in range(1, len(s)//2 + 1):
        result = ''
        tmp = s[:i]  # 현재 비교할 문자열 단위
        cnt = 1  # 반복 횟수

        # 문자열을 단위 크기만큼 순회하며 압축
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:  # 이전 단위와 같다면
                cnt += 1  # 반복 횟수 증가
            else:  # 다른 단위를 만났을 때
                if cnt > 1:
                    result += str(cnt) + tmp  # 반복 횟수와 단위 추가
                else:
                    result += tmp  # 단위만 추가
                cnt = 1  # 반복 횟수 초기화
                tmp = s[j:j+i]  # 새로운 비교 단위 설정

        # 마지막 단위 처리
        if cnt > 1:
            result += str(cnt) + tmp
        else:
            result += tmp

        answer.append(len(result))  # 압축된 문자열의 길이 저장

    return min(answer)  # 가장 짧은 압축 길이 반환