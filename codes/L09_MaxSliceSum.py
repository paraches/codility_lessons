def solution(A: [int]) -> int:
    max_value = -1000000
    sum_value = 0

    for i in A:
        sum_value += i
        if sum_value > max_value:
            max_value = sum_value
        if sum_value < 0:
            sum_value = 0

    return max_value
