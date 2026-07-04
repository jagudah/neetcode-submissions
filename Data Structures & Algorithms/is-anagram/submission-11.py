class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = Counter(s)

        for c in t:
            temp = sCount.get(c, 0)
            if temp == 0:
                return False
            sCount[c] -= 1

        for num in sCount.values():
            if num > 0:
                return False

        return True 