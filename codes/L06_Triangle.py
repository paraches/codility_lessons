def solution(A: [int]) -> int:
    if len(A) < 3:
        return 0

    A.sort()

    for i in reversed(range(2, len(A))):
        pv = A[i-2]
        qv = A[i-1]
        rv = A[i]

        if pv < 0:
            return 0

        if pv + qv > rv:
            return 1

    return 0
