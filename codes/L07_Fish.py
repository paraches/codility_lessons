def solution(A: [int], B: [int]) -> int:
    downstream_fishes = []
    alive_fish = 0

    for size, direction in zip(A, B):
        if direction == 1:
            downstream_fishes.append(size)
        else:
            while len(downstream_fishes) > 0:
                if downstream_fishes[-1] > size:
                    break
                else:
                    downstream_fishes.pop()
            if len(downstream_fishes) == 0:
                alive_fish += 1

    return alive_fish + len(downstream_fishes)
