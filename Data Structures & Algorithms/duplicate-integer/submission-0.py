class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        curr = 0
        next = 1
        while curr < len(nums) - 1:
            if nums[curr] == nums[next]:
                return True
            else:
                next += 1
                if next == len(nums):
                    curr += 1
                    next = curr + 1
        return False