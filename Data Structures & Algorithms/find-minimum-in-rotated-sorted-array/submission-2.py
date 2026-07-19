class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minNum = 1000

        while l <= r:
            m = (l + r) // 2
            
            if nums[r] < nums[m]:
                l = m + 1
            elif nums[l] < nums[m]:
                r = m - 1
            else:
                minNum = min(minNum, nums[m])
                r -= 1
        return minNum