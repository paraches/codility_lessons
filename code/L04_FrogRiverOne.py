def solution(X: int, A: [int]) -> int:
    pool = set()

    for i, v in enumerate(A):
        pool.add(v)
        if len(pool) == X:
            return i

    return -1
