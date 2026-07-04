from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCounter = Counter(s)
        tCounter = Counter(t)

        for char in s:
            if sCounter[char] != tCounter[char]:
                return False

        return True