class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        i, j = 0, 0
        res = 0
        while j < len(s):
            if s[j] in hashSet:
                while s[j] in hashSet:
                    hashSet.remove(s[i])
                    i += 1
            hashSet.add(s[j])
            res = max(res, j-i+1)
            j += 1
        return res