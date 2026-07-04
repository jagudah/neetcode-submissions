class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count, result = 0, 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                while (num + count) in numSet:
                    count += 1
                result = max(result, count)
            count = 0
        
        return result