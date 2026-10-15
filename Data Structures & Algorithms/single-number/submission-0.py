class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = [False] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    found[i], found[j] = True, True
            if found[i] == False:
                return nums[i]
        return -1