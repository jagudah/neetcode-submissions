class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set()
        for num in nums:
            numSet.add(num)
        for num in numSet:
            if (num - 1) not in numSet:
                temp = 0
                while (num + temp) in numSet:
                    temp += 1
                res = max(res, temp)
        return res