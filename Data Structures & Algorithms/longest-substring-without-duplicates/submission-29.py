class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        i, result = 0, 0

        for j in range(len(s)):
            if s[j] in charSet:
                while s[j] in charSet:
                    charSet.remove(s[i])
                    i += 1
            charSet.add(s[j])
            result = max(result, j-i+1)
        return result