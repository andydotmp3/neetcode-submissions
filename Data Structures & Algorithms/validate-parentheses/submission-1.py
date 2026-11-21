class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairings = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        pairings_reverse = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in pairings:
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            if stack[-1] != pairings_reverse[char]:
                return False
            stack = stack[:-1]
        return len(stack) == 0
