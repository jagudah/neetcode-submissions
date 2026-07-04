class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in hashMap:
                if len(stack) == 0:
                    return False
                temp = stack.pop()

                if hashMap[c] != temp:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0