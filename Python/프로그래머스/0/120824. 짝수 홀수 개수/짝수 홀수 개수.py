def solution(num_list):
    #각각의 홀수 짝수 의 담을 배열을 리턴할 배열
    even_count = 0
    odd_count = 0
    #리스트에서 숫자 하나씩 꺼내기
    for num in num_list:
        #짝수 촐수에 대해서 판별하는 조건문
        if num %2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return [even_count, odd_count]