class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        i, res = 0, 0
        for j in range(i, len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            res = max(res, len(charSet))
        return res