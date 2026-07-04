class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1

        while l < len(numbers) - 1:
            temp = numbers[l] + numbers[r]
            if (temp == target):
                return [l+1, r+1]
            if (r == len(numbers) - 1):
                l += 1
                r = l + 1
                continue
            r += 1
            