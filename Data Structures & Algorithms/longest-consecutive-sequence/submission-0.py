class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        count = 0
        nums.sort()
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                count = 0
                while (num + count) in numSet:
                    count += 1
                maxSeq = max(maxSeq, count)

        return maxSeq