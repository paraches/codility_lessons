def solution(A: [int]) -> int:
    max_revenue = 0
    min_value = 200000

    for v in A:
        if min_value > v:
            min_value = v
        else:
            revenue = v - min_value
            if revenue > max_revenue:
                max_revenue = revenue

    return max_revenue
