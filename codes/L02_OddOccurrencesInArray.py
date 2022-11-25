def solution(A: [int]) -> int:
    pool = set()
    for i in A:
        if i in pool:
            pool.remove(i)
        else:
            pool.add(i)

    return pool.pop()
