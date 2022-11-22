def solution(A: [int]) -> int:
    A.sort()

    for i, v in enumerate(A):
        if i + 1 != v:
            return 0

    return 1
