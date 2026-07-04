class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        parMap = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        stack = []

        for par in s:
            if par in parMap:
                stack.append(par)
            else:
                lastElem = stack.pop() if len(stack) > 0 else 0
                rightPar = parMap.get(lastElem, 0)

                if rightPar != par:
                    return False
        
        return len(stack) == 0
