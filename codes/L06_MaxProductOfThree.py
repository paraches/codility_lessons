def solution(A: [int]) -> int:
    if len(A) == 3:
        return A[0] * A[1] * A[2]

    A.sort()

    if A[-3] > 0:
        ppp = A[-3] * A[-2] * A[-1]
        if A[1] < 0:
            pnn = A[-1] * A[0] * A[1]
            return ppp if ppp > pnn else pnn
        else:
            return ppp
    elif A[-1] > 0 > A[1]:
        pnn = A[-1] * A[0] * A[1]
        return pnn
    elif A[-1] == 0 or A[-3] == 0:
        return 0
    else:
        return A[-1] * A[-2] * A[-3]
