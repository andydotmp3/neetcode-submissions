class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            value = None
            match token:
                case "+":
                    value = stack[-2] + stack[-1]
                case "-":
                    value = stack[-2] - stack[-1]
                case "*":
                    value = stack[-2] * stack[-1]
                case "/":
                    value = int(stack[-2] / stack[-1])
            if value is not None:
                stack[-2] = value
                stack = stack[:-1]
                continue


            stack.append(int(token))
            
        return stack[0]