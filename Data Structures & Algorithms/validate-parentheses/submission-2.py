from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = deque()
        for char in s:
            if char == "(" or char == "[" or char == "{":
                parentheses_stack.appendleft(char)
            else:
                if not parentheses_stack:
                    return False
                pop = parentheses_stack.popleft()
                if (pop == "(" and char != ")") or (pop == "[" and char != "]") or (pop == "{" and char != "}"):
                    return False

        return not parentheses_stack
