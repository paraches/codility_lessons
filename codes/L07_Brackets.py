def solution(S: str) -> int:
    right_brackets = [')', ']', '}']
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for i in S:
        if i in right_brackets:
            if len(stack) > 0:
                left_bracket = stack.pop()
                if bracket_dict[left_bracket] != i:
                    return 0
            else:
                return 0
        else:
            stack.append(i)

    return 1 if len(stack) == 0 else 0
