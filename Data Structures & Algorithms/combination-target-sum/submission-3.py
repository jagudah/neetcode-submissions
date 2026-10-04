class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, curr, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                result.append(curr.copy())
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()
        dfs(0, [], 0)
        return result