class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(numbers):
            temp = target - num
            if temp in mp:
                return [mp[temp] + 1, i+1]
            mp[num] = i