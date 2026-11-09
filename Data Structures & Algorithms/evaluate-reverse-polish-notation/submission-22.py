class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set('+-/*')
        stack = []

        for t in tokens:
            if t in ops:
                b, a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                if t == '*':
                    stack.append(a * b)
                if t == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[-1]