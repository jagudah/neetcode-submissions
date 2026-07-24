class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] < nums[r]:
                r -= 1
            elif nums[l] > nums[r]:
                l  += 1
            else:
                return nums[m]
        return -1