def solution(K: int, A: [int]) -> int:
    count = 0
    index = 0
    v_sum = 0

    while index < len(A):
        v_sum += A[index]
        if v_sum >= K:
            count += 1
            v_sum = 0
        index += 1

    return count
