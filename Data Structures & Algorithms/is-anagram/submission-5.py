class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = Counter(s)

        for char in t:
            if char in sCount and sCount[char] > 0:
                sCount[char] -= 1
            else:
                return False
        
        return True