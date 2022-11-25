def solution(S: str) -> int:
    stack = []

    for i in S:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0

    return 1 if len(stack) == 0 else 0
