# 같은 값 연속해서 나타나는 것 
# -> 해당 문자 개수(여러 문자 단위 가능) + 해당 문자
def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        result = ''
        tmp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + tmp
                else:
                    result += tmp
                cnt = 1
                tmp = s[j:j+i]
        if cnt > 1:
            result += str(cnt) + tmp
        else:
            result += tmp
        answer.append(len(result))
    return min(answer)