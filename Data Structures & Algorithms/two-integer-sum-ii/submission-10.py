class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(numbers):
            temp = hashMap.get(target-num, 0)
            if temp > 0:
                return [temp, i+1]
            hashMap[num] = i + 1