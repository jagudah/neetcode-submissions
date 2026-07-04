class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count, result = 0, 0

        for num in nums:
            if (num - 1) not in numSet:
                while (num + count) in numSet:
                    count += 1
                result = max(result, count)
            count = 0
        
        return result