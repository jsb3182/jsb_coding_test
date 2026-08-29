def solution(numbers):
    answer = [] #결과를 담을 빈리스트를 생성합니다
    #numbers 리스트에서 원소를 하나씩 num이라는 이름으로 꺼냅
    for num in numbers:
        answer.append(num * 2)
    return answer