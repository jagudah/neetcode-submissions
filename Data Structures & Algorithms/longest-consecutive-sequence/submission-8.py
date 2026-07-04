class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for num in numSet:
            if (num - 1) not in numSet:
                count = 1
                while (num + 1) in numSet:
                    num += 1
                    count += 1
                result = max(count, result)
        
        return result