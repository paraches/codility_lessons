def solution(M: int, A: [int]) -> int:
    count = 0
    index = 0
    base = 0
    pool = set()

    while index < len(A):
        while index < len(A) and A[index] not in pool:
            count += index - base + 1
            pool.add(A[index])
            index += 1
        while index < len(A) and A[base] != A[index]:
            pool.remove(A[base])
            base += 1
        pool.remove(A[base])
        base += 1

    return min(count, 1000000000)
