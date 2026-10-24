class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        if target in hashSet:
            return True
        return False