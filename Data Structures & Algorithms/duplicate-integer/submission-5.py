class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        counter = defaultdict(int)

        for num in nums:
            if counter[num] != 0:
                return True
            counter[num] += 1
        
        return False