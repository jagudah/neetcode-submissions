class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = set()
        for num in nums:
            if num in found:
                found.discard(num)
            else:
                found.add(num)
        return found.pop()