def solution(money):
    answer = [] #출력할 배열 출력해야되는것 [] 리스트안에 이제 나머지랑 이제 몫이랑 나머지 출력합니다.
    answer = [money // 5500, money % 5500]
    return answer