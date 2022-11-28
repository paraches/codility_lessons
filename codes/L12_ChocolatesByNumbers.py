def solution(N: int, M: int) -> int:
    a = M * N
    m = M

    if N > M:
        M, N = N, M

    while N != 0:
        M, N = N, M % N

    return int(a / M / m)
