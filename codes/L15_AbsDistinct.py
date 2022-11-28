def solution(A: [int]) -> int:
    pool = set()

    for i in A:
        pool.add(abs(i))

    return len(pool)
