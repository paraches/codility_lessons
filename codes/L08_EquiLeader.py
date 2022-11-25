def solution(A: [int]) -> int:
    value_dic = {}
    for i, v in enumerate(A):
        if v in value_dic.keys():
            value_dic[v].append(i)
        else:
            value_dic[v] = [i]

    leader_index_array = max(value_dic.values(), key=lambda x: len(x))
    leader_count = len(leader_index_array)
    equi_leader_count = 0

    index = 0
    left_leader_count = 0
    for leader_index in leader_index_array:
        while index <= leader_index:
            if index == leader_index:
                left_leader_count += 1
            left_size = index + 1
            right_size = len(A) - left_size
            right_leader_count = leader_count - left_leader_count
            if left_leader_count > int(left_size / 2) and right_leader_count > int(right_size / 2):
                equi_leader_count += 1
            index += 1

    return equi_leader_count
