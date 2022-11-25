def solution(A: [int]) -> int:
    if len(A) == 0:
        return -1

    a = [(i, v) for i, v in enumerate(A)]
    a.sort(key=lambda x: x[1])

    max_count = 0
    pre_i, pre_v = a[0]
    max_value_index = pre_i

    count = 0
    for i, v in a:
        if v == pre_v:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_value_index = pre_i
            count = 1
            pre_i, pre_v = i, v

    if count > max_count:
        max_count = count
        max_value_index = pre_i

    return max_value_index if max_count > len(A) / 2 else -1
