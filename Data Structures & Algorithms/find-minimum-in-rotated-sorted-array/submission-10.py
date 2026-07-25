class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = 1000

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] > nums[l]:
                r = m - 1
            else:
                minNum = min(minNum, nums[m])
                r = m -1 
        
        return minNum