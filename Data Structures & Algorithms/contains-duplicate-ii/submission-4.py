class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)

        if length == 1:
            return False

        hashMap = {}
        for i in range(length):
            if nums[i] in hashMap and abs(hashMap[nums[i]] - i) <= k:
                return True
            hashMap[nums[i]] = i
        return False