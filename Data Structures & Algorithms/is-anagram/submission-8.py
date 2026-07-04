class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = Counter(s)

        for char in t:
            if sCount.get(char, 0) == 0:
                return False
            else:
                sCount[char] -= 1
        
        return True