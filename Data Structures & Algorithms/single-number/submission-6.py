class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numCount = collections.Counter(nums)
        for num in numCount:
            if numCount[num] == 1:
                return num
        return -1