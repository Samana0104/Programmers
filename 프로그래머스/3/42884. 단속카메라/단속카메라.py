def solution(routes):
    answer = 0
    observe_value = []

    routes.sort(key=lambda x: x[0])
    observe_value = routes[0]
    
    observe_start = routes[0][0]
    observe_end = routes[0][1]

    camera_num = 0

    for i in range(0, len(routes)):
        next_start = routes[i][0]
        next_end = routes[i][1]

        if next_start <= observe_end:
            observe_start = max(observe_start, next_start)
            observe_end = min(observe_end, next_end)
        else:
            camera_num += 1
            observe_start = routes[i][0]
            observe_end = routes[i][1]

    camera_num += 1
    answer = camera_num
    return answer