class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        for num in nums:
            if num == target:
                return True
        return False