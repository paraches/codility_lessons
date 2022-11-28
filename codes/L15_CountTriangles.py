def solution(A: [int]) -> int:
    sorted_a = sorted(A)
    count = 0

    for i in reversed(range(len(A))):
        min_index = 0
        max_index = i - 1

        while min_index < max_index:
            if sorted_a[min_index] + sorted_a[max_index] > sorted_a[i]:
                count += max_index - min_index
                max_index -= 1
            else:
                min_index += 1

    return count
