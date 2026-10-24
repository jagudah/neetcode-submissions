class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        i, res = 0, 0
        for num in numSet:
            if (num - 1) not in numSet:
                while (num + i) in numSet:
                    i += 1
                res = max(res, i)
                i = 0
        return res