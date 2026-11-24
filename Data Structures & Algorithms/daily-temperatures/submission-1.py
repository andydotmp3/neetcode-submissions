class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        i = len(temperatures) - 1
        for temp in reversed(temperatures):
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if not stack:
                result.append(0)
            else:
                result.append(stack[-1][1] - i)
            stack.append((temp, i))
            i -= 1
        
        result.reverse()
            
        return result