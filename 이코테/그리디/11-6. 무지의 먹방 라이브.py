def solution(food_times, k):
    answer = 0

    i = 0
    while True:

        if k == -1:
            answer = i
            break
        else:
            i = i % len(food_times)
            if (food_times[i] != 0):
                food_times[i] -= 1
                k -= 1
        i += 1

    return answer
    
    # 정확성 점수는 37.7
    # 효율성 점수는 0 점 -> 모두 시간 초과가 났으므로 다른 방법을 생각해야 함.
