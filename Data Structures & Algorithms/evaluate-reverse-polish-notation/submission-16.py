class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+','-','*','/'}
        stack = []

        for c in tokens:
            print("Stack: " + str(stack))
            if c in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                if c == '+':
                    stack.append(str(a + b))
                elif c == '-':
                    stack.append(str(a - b))
                elif c == '*':
                    stack.append(str(a * b))
                else:
                    b = float(b)
                    a = float(a)
                    stack.append(str(int(a / b)))
            else:
                stack.append(c)
        return int(stack.pop())