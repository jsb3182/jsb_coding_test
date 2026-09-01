def solution(my_string, overwrite_string, s): #매개변수 3개
    front = my_string[:s]
    middle = overwrite_string
    back = my_string[s + len(overwrite_string):]
    return front + middle + back