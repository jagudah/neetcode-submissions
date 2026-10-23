class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        hashSet = set()
        i, res = 0, 0
        for j in range(i, len(nums)):
            if nums[j] in hashSet:
                continue
            if nums[j] not in hashSet and nums[j] != nums[j-1] + 1:
                hashSet.clear()
                i = j
            hashSet.add(nums[j])
            res = max(res, len(hashSet))
        return res