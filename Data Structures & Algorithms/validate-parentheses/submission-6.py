class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for char in s:
            if char in hashMap:
                stack.append(char)
            else:
                if len(stack) > 0 and hashMap[stack[-1]] is char:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        
        return len(stack) == 0