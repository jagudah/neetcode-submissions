class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''Setup: Initialize res array and sort candidates list to filter out nums that will exceed target'''
        candidates.sort()
        self.res = []
        
        '''DFS function to recursively append nums to subset that equate to target'''
        def dfs(i, curr, total):
            if total == target:
                self.res.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(j+1, curr, total + candidates[j])
                curr.pop()
        
        '''Call DFS function and return self.res'''
        dfs(0, [], 0)
        return self.res