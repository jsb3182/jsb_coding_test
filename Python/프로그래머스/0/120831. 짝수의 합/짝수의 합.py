def solution(n):
    answer = 0 #초기화
    for i in range(2, n+ 1, 2):
        answer += i #합
    return answer