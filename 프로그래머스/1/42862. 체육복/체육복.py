def solution(n, lost, reserve):
    # 중복된 학생 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 앞번호 학생부터 체육복 빌려주기
    for student in sorted(reserve_set):
        if student - 1 in lost_set:
            lost_set.remove(student - 1)
        elif student + 1 in lost_set:
            lost_set.remove(student + 1)

    # 체육수업을 들을 수 있는 학생 수 계산
    return n - len(lost_set)