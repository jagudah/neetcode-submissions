class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 > 0:
            return False
        sList = []
        hashMap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in hashMap:
                sList.append(char)
            else:
                if len(sList) == 0 or hashMap[sList[-1]] != char:
                    return False
                sList.pop()

        return len(sList) == 0