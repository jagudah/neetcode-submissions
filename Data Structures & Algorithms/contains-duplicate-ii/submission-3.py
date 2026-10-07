class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length == 1:
            return False
        i, j = 0, 1
        while j < length:
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
            if j + 1 == length:
                i += 1
                j = i
            j += 1
        return False