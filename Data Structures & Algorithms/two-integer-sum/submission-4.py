class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for i, n in enumerate(nums):
            temp = target - n

            if temp in hashMap:
                return [hashMap[temp], i]
            hashMap[n] = i