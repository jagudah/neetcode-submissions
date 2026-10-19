class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = set()
        i, res = 0, 0
        for j in range(i, len(s)):
            if s[j] in found:
                while s[j] in found:
                    found.remove(s[i])
                    i += 1
            found.add(s[j])
            res = max(res, len(found))
        return res