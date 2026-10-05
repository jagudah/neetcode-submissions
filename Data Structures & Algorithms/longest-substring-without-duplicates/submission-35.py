class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            res = max(r-l+1, res)
            r += 1
        return res