def solution(n, times):
    answer = 0
    
    min_time = 0
    max_time = 0
    
    for examiner in times:
        if examiner*n >= max_time:
            max_time = examiner*n

    left = 0
    right = max_time
    mid = 0
    
    weight = 0

    while left<=right:
        mid = int((left+right)*0.5)
        weight = 0

        for examiner in times:
            weight += mid // examiner

        if weight >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    
    return answer