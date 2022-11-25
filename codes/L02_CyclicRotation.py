def solution(A: [int], K: int) -> [int]:
    a_length = len(A)
    if a_length == 0 or K == 0:
        return A

    k = K % a_length
    if k == 0:
        return A

    right_array = A[:a_length - k]
    left_array = A[-k:]

    return left_array + right_array
