class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i == len(nums):
                return
            if total + nums[i] <= target:
                cur.append(nums[i])
                backtrack(i, cur, total+nums[i])
                cur.pop()
                backtrack(i+1, cur, total)
        backtrack(0, [], 0)
        return res