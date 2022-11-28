import math


def solution(N: int) -> int:
    factors = {1, N}

    s = math.sqrt(N)
    for i in range(2, int(s) + 1):
        if N % i == 0:
            factors.add(i)
            factors.add(int(N / i))

    print(f'factors: {factors}')
    return len(factors)
