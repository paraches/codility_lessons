def solution(A: [int]) -> int:
    pool = set()

    for i in A:
        pool.add(i)

    return len(pool)
