def solution(array):
    # 각 숫자의 등장 횟수를 저장할 빈 딕셔너리 생성 (예: {숫자: 빈도수})
    frequency = {}
    
    # 1단계: 배열의 모든 숫자를 순회하며 등장 횟수 카운트
    for num in array:
        # 이미 딕셔너리에 존재하는 숫자라면 카운트 +1
        if num in frequency:
            frequency[num] += 1
        # 처음 등장한 숫자라면 딕셔너리에 추가하고 1로 초기화
        else:
            frequency[num] = 1

    # 2단계: 딕셔너리에 기록된 빈도수(value) 중 가장 큰 값(최대 등장 횟수) 탐색
    max_freq = max(frequency.values())
    
    # 3단계: 리스트 컴프리헨션을 사용해 최대 빈도수(max_freq)를 가진 숫자(key)들을 추출
    mode_candidates = [k for k, v in frequency.items() if v == max_freq]

    # 4단계: 최빈값 개수에 따른 결과 반환
    # 최빈값을 가진 숫자가 2개 이상이면 -1 반환
    if len(mode_candidates) > 1:
        return -1
    # 최빈값이 유일하다면 해당 숫자 반환
    else:
        return mode_candidates[0]