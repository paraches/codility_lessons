def solution(A: [int]) -> int:
    a_sum = sum(A)
    min_delta = 2000

    left_sum = 0
    for i in range(len(A)-1):
        left_sum += A[i]
        right_sum = a_sum - left_sum
        delta = abs(left_sum - right_sum)
        if delta < min_delta:
            min_delta = delta

    return min_delta
