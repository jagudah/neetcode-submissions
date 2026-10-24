class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        i, res = 0, 0
        for j in range(i, len(s)):
            if s[j] in hashSet:
                while s[j] in hashSet:
                    hashSet.remove(s[i])
                    i += 1
            hashSet.add(s[j])
            res = max(res, j-i+1)
        return res