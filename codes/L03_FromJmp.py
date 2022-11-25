def solution(X: int, Y: int, D: int) -> int:
    distance = Y - X
    jump = int(distance / D)
    return jump + 1 if distance % D else jump
