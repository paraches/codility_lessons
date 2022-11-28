import math


def solution(N: int) -> int:
    s = int(math.sqrt(N))

    for i in reversed(range(1, s + 1)):
        if N % i == 0:
            return (i + int(N / i)) * 2

    return (1 + N) * 2
