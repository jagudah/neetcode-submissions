class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        numSet = set(nums)
        for num in nums:
            if (num - 1) not in numSet:
                count = 0
                while (num + count) in numSet:
                    count += 1
                result = max(count, result)

        return result