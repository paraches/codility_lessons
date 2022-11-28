def solution(A: [int], B: [int]) -> int:
    if len(A) < 2:
        return len(A)

    count = 1
    end_number = B[0]

    for i in range(len(A)):
        if A[i] > end_number:
            count += 1
            end_number = B[i]

    return count

