class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        curr, res = 0, 0

        for num in hashSet:
            if (num - 1) not in hashSet:
                while (num + curr) in hashSet:
                    curr += 1
                res = max(res, curr)
                curr = 0
        return res