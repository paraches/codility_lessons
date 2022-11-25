def solution(A: [int]) -> int:
    east_car = 0
    passing = 0

    for i in A:
        if i == 1:
            passing += east_car
        else:
            east_car += 1

    if passing > 1000000000:
        passing = -1

    return passing
