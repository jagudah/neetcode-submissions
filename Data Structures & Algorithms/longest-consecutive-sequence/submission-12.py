class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        curr, res = 0, 0

        for num in hashSet:
            if (num - 1) not in hashSet:
                i = 0
                while (num + i) in hashSet:
                    curr += 1
                    i += 1
                res = max(res, curr)
                curr = 0
        return res