class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        charMap = {}
        result = 0

        while r < len(s):
            if s[r] in charMap:
                result = max(result, r - l)
                while s[r] in charMap:
                    del charMap[s[l]]
                    l += 1
            charMap[s[r]] = r
            r += 1
        result = max(result, r - l)
        return result