class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = set()
        l, r = 0, 0
        result = 0

        while r < len(s):
            if s[r] in charMap:
                while s[r] in charMap:
                    charMap.remove(s[l])
                    l += 1
            charMap.add(s[r])
            result = max(result, r-l+1)
            r += 1
        return result